"""
Landmark Search Index
---------------------

Builds a Whoosh search index from fullDatabase.csv and allows users
to search landmark records from the command line.

Dataset columns:
Name, Size, Location, Longitude, Latitude, Image, Type, Description
"""

from pathlib import Path
import csv
import shutil

from whoosh.fields import ID, TEXT, Schema
from whoosh.index import create_in
from whoosh.qparser import MultifieldParser


DATA_FILE = Path("fullDatabase.csv")
INDEX_DIR = Path(".whoosh_index")
RESULT_LIMIT = 10


def build_index(data_file=DATA_FILE, index_dir=INDEX_DIR):
    """Create a fresh Whoosh index from the landmark CSV file."""
    if not data_file.exists():
        raise FileNotFoundError(f"Could not find dataset: {data_file}")

    if index_dir.exists():
        shutil.rmtree(index_dir)

    index_dir.mkdir(parents=True, exist_ok=True)

    schema = Schema(
        record_id=ID(stored=True),
        Name=TEXT(stored=True),
        Size=TEXT(stored=True),
        Location=TEXT(stored=True),
        Longitude=TEXT(stored=True),
        Latitude=TEXT(stored=True),
        Image=TEXT(stored=True),
        Type=TEXT(stored=True),
        Description=TEXT(stored=True),
    )

    search_index = create_in(index_dir, schema)
    writer = search_index.writer()

    with data_file.open("r", encoding="utf-8", newline="") as csvfile:
        reader = csv.reader(csvfile)
        row_count = 0

        for row_count, row in enumerate(reader, start=1):
            if len(row) < 8:
                continue

            writer.add_document(
                record_id=str(row_count),
                Name=row[0],
                Size=row[1],
                Location=row[2],
                Longitude=row[3],
                Latitude=row[4],
                Image=row[5],
                Type=row[6],
                Description=row[7],
            )

    writer.commit()
    print(f"Total Tuples Indexed: {row_count}")
    return search_index


def search_landmarks(search_index, search_term, limit=RESULT_LIMIT):
    """Search the landmark index and print ranked results."""
    searchable_fields = ["Name", "Location", "Type", "Size", "Description"]

    with search_index.searcher() as searcher:
        parser = MultifieldParser(searchable_fields, schema=search_index.schema)
        query = parser.parse(search_term)
        results = searcher.search(query, limit=limit)

        print(f"Length of results: {len(results)}")

        if not results:
            print("No matching landmarks found.")
            return

        for rank, result in enumerate(results, start=1):
            print(f"\n{rank}. {result['Name']}")
            print(f"   Type: {result['Type']}")
            print(f"   Size: {result['Size']}")
            print(f"   Location: {result['Location']}")
            print(f"   Coordinates: {result['Latitude']}, {result['Longitude']}")
            print(f"   Image: {result['Image']}")
            print(f"   Description: {result['Description'][:250]}...")


def main():
    search_index = build_index()

    print("\nLandmark Search")
    print("Type a search term to query the database.")
    print("Type 'exit' to quit.\n")

    while True:
        search_term = input("Please enter a query: ").strip()

        if search_term.lower() == "exit":
            print("Goodbye.")
            break

        if not search_term:
            print("Please enter a search term.")
            continue

        search_landmarks(search_index, search_term)


if __name__ == "__main__":
    main()
