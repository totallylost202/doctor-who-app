import json
from dotenv import load_dotenv
import requests
import os
import pandas as pd
import sqlite3

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

if API_KEY is None:
    print("TMDB_API_KEY was not found.")
    exit()

"""while True:
    try:
        season = int(input("Enter a season number (1-15): "))

        if 1 <= season <= 15:
            break

        print("Please enter a number between 1 and 15.")

    except ValueError:
        print("Please enter a number between 1 and 15.")

        """

params = {

    "api_key": API_KEY

}

all_episodes = []

show_url = "https://api.themoviedb.org/3/tv/57243"

response = requests.get(show_url, params=params)
response.raise_for_status()

show_data = response.json()

for season_info in show_data["seasons"]:
    season = season_info["season_number"]

    url = f"https://api.themoviedb.org/3/tv/57243/season/{season}"

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    for episode in data["episodes"]:
        all_episodes.append({
            "season": season,
            "episode": episode["episode_number"],
            "title": episode["name"],
            "rating": episode["vote_average"]
        })

with open("all_episodes.json", "w") as f:

    json.dump(all_episodes, f, indent=2)


df = pd.DataFrame(all_episodes)

conn = sqlite3.connect("doctor_who.db")

df.to_sql(
    "episodes",
    conn,
    if_exists="replace",
    index=False
)

conn.close()