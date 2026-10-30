import sqlite3
import unittest
from search import search_db

class TestDoctorWhoSearch(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE episodes (
                season INTEGER,
                episode INTEGER,
                title TEXT,
                rating REAL
            )
        """)

        self.cursor.executemany("""
            INSERT INTO episodes (season, episode, title, rating)
            VALUES (?, ?, ?, ?)
        """, [
            (6, 1, "Episode A", 8.2),
            (6, 2, "Episode B", 9.1),
            (5, 1, "Episode C", 7.5)
        ])

        self.conn.commit()

    def test_search_returns_correct_number_of_episodes(self):
        rows = search_db(self.cursor, 6)

        self.assertEqual(len(rows), 2)

    def test_search_orders_episodes_by_rating(self):
        rows = search_db(self.cursor, 6)

        self.assertEqual(rows[0][2], "Episode B")

    def test_search_returns_empty_list_for_unknown_season(self):
        rows = search_db(self.cursor, 999)

        self.assertEqual(rows, [])

    def test_search_returns_at_most_ten_episodes(self):
        for episode_number in range(3, 14):
            self.cursor.execute("""
                INSERT INTO episodes (season, episode, title, rating)
                VALUES (?, ?, ?, ?)
            """, (
                6,
                episode_number,
                f"Episode {episode_number}",
                7.0
            ))

        self.conn.commit()

        rows = search_db(self.cursor, 6)

        self.assertEqual(len(rows), 10)

    def tearDown(self):
        self.conn.close()

if __name__ == "__main__":
    unittest.main()