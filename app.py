import os
import sqlite3
import sys
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.db")


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY, at TEXT)")
    return conn


@app.get("/")
def index():
    return jsonify(
        framework="Flask",
        python=sys.version.split()[0],
        time=datetime.now(timezone.utc).isoformat(),
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/visits")
def visits():
    """Kalıcı SQLite dosyası testi: her istekte bir satır ekler."""
    conn = db()
    conn.execute("INSERT INTO visits (at) VALUES (?)", (datetime.now(timezone.utc).isoformat(),))
    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM visits").fetchone()[0]
    conn.close()
    return jsonify(visits=count)


if __name__ == "__main__":
    app.run(debug=True)
