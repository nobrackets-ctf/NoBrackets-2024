#!/usr/bin/env python3

import sqlite3

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            voted BOOLEAN NOT NULL
        )
    ''')
    # Le hash est le même sur le serveur, dans tous les cas c'est un hash donc c'est sécurisé, non ?
    cursor.execute('''
        INSERT INTO users (username, password, voted) VALUES ('admin', '1e6b41f0261eed5acd27bd7d0f6463389a420219981572546e6ca1b34188ebc2', 0)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()