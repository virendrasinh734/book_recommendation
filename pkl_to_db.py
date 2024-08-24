import pickle
import sqlite3
import pandas as pd

pickle_file = 'combined_cosine_sim_matrix.pkl'
sqlite_file = 'your_database.db'

with open(pickle_file, 'rb') as f:
    data = pickle.load(f)

if not isinstance(data, pd.DataFrame):
    data = pd.DataFrame(data)

conn = sqlite3.connect(sqlite_file)

table_name = 'combined_cosine_sim_matrix'
data.to_sql(table_name, conn, if_exists='replace', index=False)

conn.close()

print(f"Data has been successfully loaded into {table_name} table in {sqlite_file}.")