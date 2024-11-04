# models.py
from datetime import datetime, timedelta
from database import get_db_connection
from random import randint

def start_new_game():
    target_number = randint(1, 1)
    start_time = datetime.utcnow()
    end_time = start_time + timedelta(hours=24)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO games (target_number, start_time, end_time) VALUES (?, ?, ?)',
                   (target_number, start_time.isoformat(), end_time.isoformat()))
    conn.commit()
    game_id = cursor.lastrowid
    conn.close()
    return game_id

def get_active_game():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM games WHERE winner IS NULL AND end_time > ?", (datetime.utcnow().isoformat(),))
    game = cursor.fetchone()
    conn.close()
    return game

def record_guess(game_id, user_id, guess):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO guesses (game_id, user_id, guess) VALUES (?, ?, ?)", (game_id, user_id, guess))
    conn.commit()
    conn.close()

def update_winner(game_id, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE games SET winner = ?, end_time = ? WHERE id = ?",
                   (user_id, datetime.utcnow().isoformat(), game_id))
    conn.commit()
    conn.close()

def save_video_path(game_id, file_location):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE games SET video_path = ? WHERE id = ?", (file_location, game_id))
    conn.commit()
    conn.close()

def get_last_completed_game():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Select only the necessary fields
    cursor.execute("SELECT id, winner, video_path, end_time FROM games WHERE winner IS NOT NULL ORDER BY end_time DESC LIMIT 1")
    
    row = cursor.fetchone()
    conn.close()
    
    # Return None if no completed game found
    if row is None:
        return None
    
    # Return as a dictionary
    return {
        "id": row[0],
        "winner": row[1],
        "video_path": row[2],
        "end_time": row[3]
    }
