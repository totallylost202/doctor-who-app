from flask import Flask, render_template, request
import sqlite3
from search import search_db

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    rows = None
    season = None
    if request.method == "POST":
        try:
            season = int(request.form.get("season"))
        except (TypeError, ValueError):
            error = "Please enter a valid number."
        else:
            conn = sqlite3.connect("doctor_who.db")
            cursor = conn.cursor()
            rows = search_db(cursor, season)
            conn.close()

    return render_template("index.html", rows=rows, season=season, error=error)

if __name__ == "__main__":
    app.run()