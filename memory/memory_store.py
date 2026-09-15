import sqlite3
from datetime import datetime

DB_PATH = "data/memory_db"

def init_memory():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS research_memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT,
        memory_type TEXT,
        content TEXT,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_memory(topic, memory_type, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO research_memory (topic, memory_type, content, created_at)
    VALUES (?, ?, ?, ?)
    """, (topic, memory_type, content, datetime.now().isoformat()))

    conn.commit()
    conn.close()

def get_memory(topic):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT memory_type, content, created_at
    FROM research_memory
    WHERE topic LIKE ?
    ORDER BY created_at DESC
    """, (f"%{topic}%",))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "memory_type": row[0],
            "content": row[1],
            "created_at": row[2]
        }
        for row in rows
    ]