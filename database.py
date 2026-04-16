import sqlite3
from datetime import datetime

def save_price(price):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price TEXT,
            timestamp TEXT
        )
    """)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO prices (price, timestamp) VALUES (?, ?)",
        (price, timestamp)
    )

    conn.commit()
    conn.close()