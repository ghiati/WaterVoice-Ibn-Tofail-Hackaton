# database.py
import sqlite3

DATABASE = 'game.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target_number INTEGER,
            start_time TEXT,
            end_time TEXT,
            winner INTEGER,
            video_path TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_id INTEGER,
            user_id INTEGER,
            guess INTEGER,
            FOREIGN KEY(game_id) REFERENCES games(id)
        )
    ''')
    conn.commit()
    conn.close()
