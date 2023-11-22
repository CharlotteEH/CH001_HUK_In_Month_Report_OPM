import pandas as pd

from connection import engine

sql_query = f"""
select distinct(OT_CGAIdent) as outlet_id,
OT_LocationDescription as location 
from OI_LIVE.dbo.vw_Outlet 
"""

df_outlet = pd.read_sql(sql_query, engine)