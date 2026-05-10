# Landmark Search Database

A Python-based landmark search project that builds a searchable database of mountains, bridges, and buildings using scraped landmark data. The project stores landmark information in a CSV file and uses Whoosh search indexing to return ranked search results.

## Project Overview

This project was designed as a searchable landmark database. A landmark is defined as an object or feature that is easily recognizable and helps people identify a location.

The database includes three landmark categories:

- Mountains
- Bridges
- Buildings

Users can search for landmarks by keyword, location, or type. The search system indexes the landmark data and returns the top matching results.

## Features

- Scrapes landmark data from Wikipedia
- Stores landmark records in a CSV database
- Uses Whoosh to build a searchable index
- Supports keyword search across multiple fields
- Returns ranked search results
- Displays landmark name, size, location, type, image link, and description
- Includes latitude and longitude fields for mapping support
- Supports landmark categories such as mountains, bridges, and buildings

## Dataset Schema

The project stores landmark data in `fullDatabase.csv`.

| Field | Description |
|---|---|
| Name | Landmark name |
| Size | Height, elevation, or length depending on landmark type |
| Location | General location text |
| Longitude | Longitude coordinate |
| Latitude | Latitude coordinate |
| Image | Image URL |
| Type | Landmark type: Mountain, Bridge, or Building |
| Description | Text description of the landmark |

## Files Included

| File | Purpose |
|---|---|
| `README.md` | Main project documentation |
| `fullScraper.py` | Scrapes landmark data from Wikipedia and saves it to CSV |
| `search_index.py` | Builds a Whoosh index and searches the landmark database |
| `fullDatabase.csv` | Landmark dataset used by the search program |
| `requirements.txt` | Python package dependencies |
| `.gitignore` | Ignores generated files, cache files, and runtime index data |
| `PROJECT_PROPOSAL.md` | Original project concept and database design summary |

## How the Search Works

The search program reads landmark records from `fullDatabase.csv`, creates a Whoosh search index, and lets the user enter search terms from the command line.

Searchable fields include:

- Name
- Location
- Type
- Size
- Description

The search returns up to 10 ranked results for each query.

## Example Searches

```bash
python search_index.py
```

Example queries:

```text
mountain Chile
bridge United States
building Asia
Everest
Mountain
```

To exit the search program, type:

```text
exit
```

## Installation

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Search Program

```bash
python search_index.py
```

The script will:

1. Read the landmark data from `fullDatabase.csv`
2. Build a local Whoosh index
3. Prompt the user for search terms
4. Print the top matching landmark results

## Running the Web Scraper

```bash
python fullScraper.py
```

The scraper collects landmark data from Wikipedia and writes results to `fullDatabase.csv`.

Note: Running the scraper can take time because it visits many Wikipedia pages. The included CSV file can be used directly if you only want to test the search feature.

## Example Output

```text
Total Tuples: 10000

Please enter a query: mountain chile
Length of results: 8

1. Acamarachi
   Type: Mountain
   Size: 6,046m (19,836ft)
   Location: Antofagasta Region, Chile
   Coordinates: 23°18′S, 67°37′W
```

## Images From Original Project

<img width="1433" alt="Landmark search screenshot 1" src="https://user-images.githubusercontent.com/39349742/207219726-7ba3a85b-8584-4570-9f7c-476de98b9299.png">

<img width="1105" alt="Landmark search screenshot 2" src="https://user-images.githubusercontent.com/39349742/207219472-4d7abcb1-c1e4-4254-b5de-da1afcacf738.png">

## Future Improvements

- Add a web interface for searching landmarks
- Display landmark results on an interactive map
- Add filters for country, continent, distance range, and landmark type
- Add pagination for large result sets
- Add better coordinate parsing for latitude and longitude
- Improve search ranking with BM25 tuning
- Add default image handling when an image URL is unavailable
- Export search results to JSON or CSV

## Technologies Used

- Python
- BeautifulSoup
- Requests
- lxml
- Whoosh
- CSV
- Wikipedia API
