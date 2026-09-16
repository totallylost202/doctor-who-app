import sqlite3

conn = sqlite3.connect("doctor_who.db")

cursor = conn.cursor()

season = int(input("Which season? "))
cursor.execute("""
    SELECT * 
    FROM episodes 
    WHERE season = ? 
    ORDER BY rating DESC
    LIMIT 10
""",(season,))

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
