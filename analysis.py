import pandas as pd
import sqlite3
from database import DB_NAME

def monthly_summary():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    if df.empty:
        print("No transactions found.")
        return

    df['date'] = pd.to_datetime(df['date'])
    summary = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
    print("\n--- Monthly Summary ---")
    print(summary)
