import sqlite3

DATABASE = "history.db"

def create_table():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS inputs (value TEXT)""")


def save_input(value):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO inputs (value) VALUES (?)", (value,))


def recent_input(limit=5):
    with sqlite3.connect(DATABASE) as conn:
        rows = conn.execute("""SELECT value FROM inputs ORDER BY rowid DESC LIMIT ?""", (limit,)).fetchall()
    return [row[0] for row in rows]


create_table()