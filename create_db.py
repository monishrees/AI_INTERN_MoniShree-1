import pandas as pd
import sqlite3

df = pd.read_csv("data_model.csv")

conn = sqlite3.connect("database.db")

df.to_sql("data_model", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully")