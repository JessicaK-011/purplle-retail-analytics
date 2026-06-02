import pandas as pd
import sqlite3

CSV_FILE = "data/Brigade_Bangalore_10_April_26.csv"

conn = sqlite3.connect("store.db")

df = pd.read_csv(CSV_FILE)

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Sales data imported successfully")