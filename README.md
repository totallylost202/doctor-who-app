# Doctor Who Episode Search

A Python application that retrieves Doctor Who episode data from the TMDB API, stores it in a SQLite database, and searches episodes by season.

## Features

- Retrieves Doctor Who episode data from TMDB
- Stores episode information in SQLite
- Searches episodes by season
- Displays the 10 highest-rated episodes

## Requirements

- Python 3
- A TMDB API key

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project folder and add your TMDB API key:

```text
TMDB_API_KEY=your_api_key_here
```

Do not upload the `.env` file to GitHub.

## Import Episode Data

Run the following command to retrieve episode information from TMDB and save it to the SQLite database:

```bash
python3 import_tmdb.py
```

This creates or updates `doctor_who.db`.

## Search Episodes

Run:

```bash
python3 search.py
```

Enter a season number when prompted:

```text
Which season? 6
```

The program displays up to 10 episodes from that season, ordered from highest to lowest rating.

## Project Structure

```text
doctor-who-app/
├── import_tmdb.py
├── search.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── doctor_who.db
├── all_episodes.json
└── doctors.json
```

## Data Source

Episode information is provided by [The Movie Database (TMDB)](https://www.themoviedb.org/).