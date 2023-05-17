"""
Cider flavours are taken from the Magners data.
"""

import pandas as pd

from connection import engine

sql_query = f"""
select distinct PT_ProductId as product_id,
    PT_ProductDescription as product,
    PT_ClassificationLevel3Description as cider_flavour
    
from PL_LIVE.dbo.vw_Product_CC_Magners
where PT_ProductId > 0
    and PT_CL5_CGA = N'Total Cider'
"""

df_cider_flavour = pd.read_sql(sql_query, engine)
