import sqlite3

def init_db():
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flag (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()

    # Insert some initial data
    cursor.execute("INSERT INTO customers (name, email) VALUES ('Alice', 'alice@cyber-corp.com')")
    cursor.execute("INSERT INTO customers (name, email) VALUES ('Bob', 'bob@cyber-corp.com')")
    cursor.execute("INSERT INTO flag (name) VALUES ('NBCTF{Automatic_query_is_fun}')")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
