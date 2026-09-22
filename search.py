import sqlite3

def get_season():
    while True:
        try:
            season = int(input("Which season? "))
            return season
        except ValueError:
            print("Please enter a number")

def search_db(cursor, season):
    cursor.execute("""
        SELECT * 
        FROM episodes 
        WHERE season = ? 
        ORDER BY rating DESC
        LIMIT 10
    """,(season,))
    rows = cursor.fetchall()
    return rows

def display_results(rows, season):
    if not rows:
        print("No episodes found for this season.")
    else:
        print(f"\nTop episodes from Season {season}\n")

        for row in rows:
            season_number, episode_number, title, rating = row
            print(f"Season {season_number}, Episode {episode_number}")
            print(title)
            print(f"Rating: {rating}")
            print("-" * 30)


def main():
    conn = sqlite3.connect("doctor_who.db")
    cursor = conn.cursor()
    season = get_season()
    rows = search_db(cursor, season)
    display_results(rows, season)
    conn.close()

if __name__ == "__main__":
    main()