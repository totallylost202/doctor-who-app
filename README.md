# Doctor Who Episode Search

A Python application that retrieves Doctor Who episode data from the TMDB API, stores it in a SQLite database, and searches episodes by season.

The project includes command-line, Streamlit, Tkinter, and Flask interfaces.

## Features

- Retrieves Doctor Who episode data from TMDB
- Stores episode information in SQLite
- Searches episodes by season
- Displays up to 10 episodes, ordered by rating
- Handles invalid input and missing results
- Provides command-line, desktop, and web interfaces

## Requirements

- Python 3
- A TMDB API key

Install the required Python packages:

```bash
python3 -m pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project folder and add your TMDB API key:

```text
TMDB_API_KEY=your_api_key_here
```

Do not upload the `.env` file to GitHub.

## Import Episode Data

Retrieve episode information from TMDB and save it to the SQLite database:

```bash
python3 import_tmdb.py
```

This creates or updates `doctor_who.db`.

## Command-Line Interface

Run:

```bash
python3 search.py
```

Enter a season number when prompted:

```text
Which season? 6
```

## Streamlit Interface

Run:

```bash
python3 -m streamlit run app.py
```

The application will open in your browser.

## Tkinter Desktop Interface

Run:

```bash
python3 tkinter_app.py
```

This opens a desktop application window.

## Flask Web Interface

Start the Flask application:

```bash
python3 flask_app.py
```

Then open the following address in your browser:

```text
http://127.0.0.1:5000
```

The Flask interface includes a styled Time Vortex-inspired background and episode result cards.

## Project Structure

```text
doctor-who-app/
├── app.py
├── flask_app.py
├── import_tmdb.py
├── search.py
├── tkinter_app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── doctor_who.db
├── all_episodes.json
└── doctors.json
```

The `.env` file is stored locally and excluded from GitHub by `.gitignore`.

## Data Source

Episode information is provided by [The Movie Database (TMDB)](https://www.themoviedb.org/).