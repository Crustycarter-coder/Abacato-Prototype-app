# database.py
import sqlite3


def connect_db():
    # This creates the file if it doesn't exist, or opens it if it does.
    return sqlite3.connect("abaca.db")


def setup_database():
    conn = connect_db()
    cursor = conn.cursor()
    # Create the users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def register_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # The "?" prevents a hack called SQL Injection
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True  # Success!
    except sqlite3.IntegrityError:
        return False  # Username already exists!
    finally:
        conn.close()


def verify_login(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()  # Fetches one matching row
    conn.close()

    if user:
        return True
    return False