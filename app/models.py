from app import app
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('transcripts.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS transcripts (url TEXT PRIMARY KEY, text TEXT)')
    conn.close()

def save_transcript(url, text):
    conn = get_db_connection()
    conn.execute('INSERT OR REPLACE INTO transcripts (url, text) VALUES (?, ?)', (url, text))
    conn.commit()
    conn.close()

def get_transcript(url):
    conn = get_db_connection()
    transcript = conn.execute('SELECT text FROM transcripts WHERE url = ?', (url,)).fetchone()
    conn.close()
    return transcript['text'] if transcript else None

init_db()
