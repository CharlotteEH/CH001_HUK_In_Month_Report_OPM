import pandas as pd

from connection import engine

sql_query = f"""
select distinct(PM_ProductItemId) as product_item_id,
PT_AT_HUK_Segment as product_segment
from WS_LIVE.dbo.vw_Epos_HUK_Weekly 
where D_DateKey >= '2022-01-01 00:00:00.000'
"""

df_segment = pd.read_sql(sql_query, engine)