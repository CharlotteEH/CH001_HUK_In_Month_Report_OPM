from pathlib import Path
import pandas as pd

from sql_query1 import df_sql_query
from sql_query2 import df_cider_flavour
from sql_query3 import df_segment
from sql_query4 import df_outlet

path = Path("Z:/PycharmProjects/CH001_HUK_In_Month_Report_OPM/b_SQL_Data_Pull")

df = pd.merge(
    df_sql_query, df_segment,
    on="product_item_id",
    how="inner"
)

df = pd.merge(
    df, df_outlet,
    on="outlet_id",
    how="inner"
)

df.to_csv(path / "data.csv", index=False)
df_cider_flavour.to_csv(path / "cider_flavour.csv", index=False)