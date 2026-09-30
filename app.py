import streamlit as st
import sqlite3
from search import search_db

st.title("Doctor Who Episode Search")
st.write("Find the highest-ranking episodes by season")

season = st.number_input("Which season?", min_value=1, step=1)

if st.button("Search"):
    conn = sqlite3.connect("doctor_who.db")
    cursor = conn.cursor()
    rows = search_db(cursor, season)
    if not rows:
        st.warning("No episodes found for this season.")
    else:
        st.subheader(f"Top episodes from Season {season}")
        for row in rows:
            season_number, episode_number, title, rating = row
            st.write(f"Season {season_number}, Episode {episode_number}")
            st.write(title)
            st.write(f"Rating: {rating}")
            st.divider()
    conn.close()