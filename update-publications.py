import json
from datetime import date

import urllib3

urllib3.disable_warnings()


INDEX_FILENAME = "_publications-index.txt"

http = urllib3.PoolManager()


queries = [
    ("Anders Børglum", 2012),
    ("Mikkel Heide Schierup", 2012),
    ("Søren Vang", 2014),
    ("Dan Søndergaard", 2015),
    ("Michael Knudsen", 2012),
    ("Søren Besenbacher", 2012),
    ("Christian N Pedersen", 2012),
    ("Thomas Mailund", 2012),
    ("Jakob Skou Pedersen", 2014),
    ("Palle Villesen", 2012),
    ("Trine Bilde", 2014),
    ("Palle Villesen", 2012),
    ("Søren Besenbacher", 2012),
    ("Michael M Hansen", 2014),
    ("Philip F Thomsen", 2014),
    ("Christian K Damgaard", 2014),
    ("Torben H Jensen", 2014),
    ("Ebbe S Andersen", 2014),
    ("Kasper Munch", 2012),
    ("Torben Asp", 2014),
]

blacklist = [
    "10.1007/s00167-019-05351-3",
    "10.12688/f1000research.15140.1",
    "10.1016/j.jtbi.2012.01.007",
    "10.1007/978-1-4419-7210-1_4",
    "10.1007/s11538-011-9658-0",
    "10.1007/s00167-013-2444-9",
    "10.1007/s00167-014-3149-4",
    "10.2106/jbjs.cc.n.00101",
    "10.1038/nature11539",
]


def disk_cache(filename="cache.json"):
    """Cache results of a function to disk based."""

    def wrapper(func):
        def cacher(*args, **kwargs):
            try:
                with open(filename) as fp:
                    cache = json.load(fp)
            except FileNotFoundError:
                cache = {}
            key = repr((args, kwargs))
            if key in cache:
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            with open(filename, "w+") as fp:
                json.dump(cache, fp)
            return result

        return cacher

    return wrapper


def search(query):
    """Search EuropePMC."""
    response = http.request(
        "GET",
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search",
        fields={"query": query, "format": "json", "pageSize": 1000,},
    )
    data = json.loads(response.data.decode("utf-8"))
    return data["resultList"]["result"]


@disk_cache(filename="_publications-cache.json")
def formatted_citation(doi, style="apa"):
    """Retrieve formatted citation from doi.org."""
    response = http.request(
        "GET",
        "https://doi.org/{}".format(doi),
        headers={"Accept": "text/x-bibliography; style={}".format(style),},
    )
    if response.status != 200:
        return None
    tmp = response.data.decode("utf-8").strip().replace("\n", "")
    return " ".join(tmp.split())


def read_index():
    try:
        with open(INDEX_FILENAME) as index_file:
            return set(line.strip() for line in index_file)
    except FileNotFoundError:
        return set()


def write_index(index):
    with open(INDEX_FILENAME, "w") as index_file:
        for doi in index:
            print(doi, file=index_file)


def diff_index(old, new):
    if not old.issubset(new):
        print("Some publications that were previously included have disappeared")
    return new.difference(old)


def main():
    index = read_index()

    total_citations = 0

    publications = []
    citations = []
    seen_ids = set()
    for author, publications_since in queries:
        for publication in search(author):
            year = int(publication["pubYear"])
            if year < publications_since:
                continue
            if publication["id"] in seen_ids:
                continue
            if "doi" not in publication:
                continue
            if publication["doi"] in blacklist:
                continue
            publications.append(publication)
            seen_ids.add(publication["id"])

            citations.append(formatted_citation(publication["doi"]))

    combined = [
        (pub, cit) for pub, cit in zip(publications, citations) if cit is not None
    ]
    new_index = set(pub["doi"] for pub, _ in combined)

    diff = diff_index(index, new_index)
    if not diff:
        print("No new publications found")
    else:
        print("The following publications were added:")
        for doi in diff:
            print("{}".format(doi))

    from collections import Counter

    c = Counter()
    j = Counter()

    print(len(combined))
    last_updated = date.today()
    with open("_publications.rst", "w") as fileobj:
        print(
            "*{} publications listed, last updated on {}*. Sorted by first publication date.".format(
                len(combined), last_updated
            ),
            file=fileobj,
        )
        print(file=fileobj)
        for publication, citation in sorted(
            combined, key=lambda p: p[0]["firstPublicationDate"], reverse=True
        ):
            total_citations += publication["citedByCount"]
            j[publication.get("journalTitle")] += 1
            c[publication["citedByCount"]] += 1

            print("* {}".format(citation), file=fileobj)

            print("(DO={})".format(publication["doi"]), end=" OR ")
            # if publication.get('journalTitle') is None:
            #    print(citation)

    write_index(new_index)

    print("Total citations: {}".format(total_citations))
    # for i, x in sorted(c.items(), key=lambda k: k[1]):
    #    print(i, x)

    for i, x in sorted(j.items(), key=lambda k: k[1]):
        if x > 1:
            print(i, x)


if __name__ == "__main__":
    main()
