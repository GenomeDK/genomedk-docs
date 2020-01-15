import json
from datetime import date

import urllib3
urllib3.disable_warnings()


INDEX_FILENAME = "_publications-index.txt"

http = urllib3.PoolManager()


queries = [
    ("Anders Børglum", 2012),
    ("Mikkel H Schierup", 2012),
    ("Søren Vang", 2016),
    ("Dan Søndergaard", 2015),
    ("Michael Knudsen", 2012),
    ("Søren Besenbacher", 2012),
    ("Christian N S Pedersen", 2012),
    ("Thomas Mailund", 2012),
]

blacklist = [
    "10.1007/s00167-019-05351-3",
    "10.12688/f1000research.15140.1",
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
        fields={
            "query": query,
            "format": "json",
            "pageSize": 1000,
        }
    )
    data = json.loads(response.data.decode("utf-8"))
    return data["resultList"]["result"]


@disk_cache(filename="_publications-cache.json")
def formatted_citation(doi, style="apa"):
    """Retrieve formatted citation from doi.org."""
    response = http.request(
        "GET",
        "https://doi.org/{}".format(doi),
        headers={
            "Accept": "text/x-bibliography; style={}".format(style),
        })
    if response.status != 200:
        return None
    return response.data.decode("utf-8").strip()


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
    assert old.issubset(new), "some publications that were previously included have disappeared"
    return new.difference(old)


def main():
    index = read_index()

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

    combined = [(pub, cit) for pub, cit in zip(publications, citations) if cit is not None]
    new_index = set(pub["doi"] for pub, _ in combined)

    diff = diff_index(index, new_index)
    if not diff:
        print("No new publications found")
        return

    print("The following publications were added:")
    for doi in diff:
        print("{}".format(doi))

    last_updated = date.today()
    with open("_publications.rst", "w") as fileobj:
        print("*{} publications listed, last updated on {}*.".format(len(combined), last_updated), file=fileobj)
        print(file=fileobj)
        for publication, citation in sorted(combined, key=lambda p: p[0]["firstPublicationDate"], reverse=True):
            print("* {}".format(citation), file=fileobj)

    write_index(new_index)


if __name__ == "__main__":
    main()
