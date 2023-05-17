from pathlib import Path

#from sql_query1 import df_sql_query
from sql_query2 import df_cider_flavour

cwd = Path(__file__).parent

#df_sql_query.to_csv(cwd / "data.csv", index=False)
df_cider_flavour.to_csv(cwd / "cider_flavour.csv", index=False)