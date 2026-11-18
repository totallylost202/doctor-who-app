import streamlit as st
import sqlite3
from search import search_db

st.html("""
<style>
    .stApp {
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.55),
                rgba(0, 0, 0, 0.55)
            ),
            url("/app/static/tardis.jpg");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    [class*="st-key-episode_card_"] {
        background-color: rgba(4, 12, 35, 0.95);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        box-shadow:
            0 14px 35px rgba(0, 0, 0, 0.65),
            0 3px 8px rgba(0, 0, 0, 0.45);
        padding: 10px;
        margin-bottom: 20px;
    }

</style>
""")

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
    for index, row in enumerate(rows, start=1):
        season_number, episode_number, title, rating, image = row

        with st.container(border=True, key=f"episode_card_{index}"):
            details_column, image_column = st.columns([3, 1])

            with details_column:
                st.subheader(
                    f"#{index}. Season {season_number}, "
                    f"Episode {episode_number}"
                )
                st.write(title)
                st.write(f"Rating: {rating:.1f}")

                if rating >= 8:
                    st.markdown(":star: :orange[**Highly rated!**] :star:")

            with image_column:
                if image:
                    st.image(image, width=220)
    conn.close()