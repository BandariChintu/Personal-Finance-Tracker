import sqlite3

DB_NAME = "finance.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(date, category, description, amount):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO transactions (date, category, description, amount) VALUES (?, ?, ?, ?)",
              (date, category, description, amount))
    conn.commit()
    conn.close()
    print("Transaction added successfully.")

def get_all_transactions():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    rows = c.fetchall()
    conn.close()
    return rows
