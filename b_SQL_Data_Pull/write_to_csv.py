from pathlib import Path

from sql_query1 import df_sql_query
from sql_query2 import df_cider_flavour

path = Path("Z:/PycharmProjects/CH001_HUK_In_Month_Report_1/b_SQL_Data_Pull")

df_sql_query.to_csv(path / "data.csv", index=False)
df_cider_flavour.to_csv(path / "cider_flavour.csv", index=False)