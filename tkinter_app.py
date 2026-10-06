import tkinter as tk
from tkinter import messagebox
import sqlite3
from search import search_db

window = tk.Tk()
window.title("Doctor Who Episode Search")

label = tk.Label(window, text="Doctor Who Episode Search")
label.pack()

season_label = tk.Label(window, text="Season")
season_entry = tk.Entry(window)
season_label.pack()
season_entry.pack()

def search():
    try:
        season = int(season_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")
        return
    conn = sqlite3.connect("doctor_who.db")
    cursor = conn.cursor()
    rows = search_db(cursor, season)
    conn.close()
    result_text.delete("1.0", tk.END)
    if not rows:
        messagebox.showinfo(
            "No Results",
            "No episodes found for this season."
        )
        return
    for row in rows:
        season_number, episode_number, title, rating = row
        result_text.insert(
            tk.END,
            f"Season {season_number}, Episode {episode_number}\n"
            f"{title}\n"
            f"Rating: {rating}\n"
            f"{'-' * 30}\n"
        )

search_button = tk.Button(
    window,
    text="Search",
    command=search
)
search_button.pack()

result_text = tk.Text(window)
result_text.pack()
window.mainloop()