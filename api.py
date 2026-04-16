from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/prices")
def get_prices():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, price, timestamp FROM prices")
    rows = cursor.fetchall()

    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "price": row[1],
            "timestamp": row[2]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)