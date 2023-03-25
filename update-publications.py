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
    ("Philip Francis Thomsen", 2021),
    ("Mads Reinholdt Jensen", 2021),
]

blacklist = [
    "10.1002/ece3.5622",
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

manually_reported_dois = [
    "10.1002/edn3.340",
    "10.1111/1755-0998.13293",
    "10.1002/edn3.193",
    "10.3389/fmars.2022.824100",
    "10.1002/edn3.285",
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


@disk_cache(filename="citations-cache.json")
def formatted_citation(doi, style="apa"):
    """Retrieve formatted citation from doi.org."""
    response = http.request(
        "GET",
        "https://doi.org/{}".format(doi),
        headers={"Accept": "text/x-bibliography; style={}".format(style),},
    )
    if response.status != 200:
        raise Exception("Could not get formatted citation")
    tmp = response.data.decode("utf-8").strip().replace("\n", "")
    return " ".join(tmp.split())


@disk_cache(filename="publications-cache.json")
def lookup_publication(doi):
    response = http.request(
        "GET",
        "https://api.crossref.org/works/{}".format(doi),
        headers={"Accept": "application/json"}
    )
    if response.status != 200:
        raise Exception("Could not look up metadata")
    return json.loads(response.data.decode("utf-8"))["message"]


def main():
    dois = set(manually_reported_dois)

    for author, publications_since in queries:
        for publication in search(author):
            doi = publication.get("doi")
            if doi is None or doi in dois:
                continue

            if publication["doi"] in blacklist:
                continue

            year = int(publication["pubYear"])
            if year < publications_since:
                continue

            dois.add(doi)

    publications = []
    for doi in dois:
        try:
            citation = formatted_citation(doi)
            if citation is None:
                continue
            metadata = lookup_publication(doi)
            published_date = tuple(metadata["published"]["date-parts"][0])
            publications.append((published_date, doi, citation))
        except Exception as exc:
            print("Skipped publication {}: {}".format(doi, exc))
            continue

    last_updated = date.today()
    with open("_publications.rst", "w") as fileobj:
        print(
            "*{} publications listed, last updated on {}*. Sorted by first publication date.".format(
                len(publications), last_updated
            ),
            file=fileobj,
        )

        print(file=fileobj)
        for _, _, citation in sorted(publications, key=lambda p: p[0], reverse=True):
            print("* {}".format(citation), file=fileobj)

if __name__ == "__main__":
    main()
