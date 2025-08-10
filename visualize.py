import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from database import DB_NAME

def plot_expenses():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    if df.empty:
        print("No transactions to plot.")
        return

    category_totals = df.groupby("category")["amount"].sum()

    plt.figure(figsize=(6, 6))
    category_totals.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expenses by Category")
    plt.ylabel("")
    plt.show()
