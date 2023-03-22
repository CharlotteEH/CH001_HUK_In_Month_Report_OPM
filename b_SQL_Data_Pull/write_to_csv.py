from pathlib import Path

from sql_query1 import df_sql_query

cwd = Path(__file__).parent

df_sql_query.to_csv(cwd / "data.csv", index=False)