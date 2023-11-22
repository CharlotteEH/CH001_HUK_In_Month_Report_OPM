# sql_query.py ---------------------------------------------------------------

""" Query to pull data
Note that will also work with the pound sign in the value column"""

import pandas as pd
from datetime import datetime as dt, timedelta as td
from connection import engine


today = dt.today()
days_ago_1 = dt.strptime("2022-01-01", "%Y-%m-%d")
days_ago_2 = today - td(days=17)

print(today)
print(days_ago_1)
print(days_ago_2)

start_date = days_ago_1.strftime('%Y-%m-%d')
end_date = days_ago_2.strftime('%Y-%m-%d')

print(start_date)
print("Until:")
print(end_date)


sql_query = f"""
select distinct(D_DateKey) as date,  
    D_Period as period,
    OT_CGAIdent as outlet_id,
    BARBLevel2Description as region, 
    OT_SegmentationLevel1Description as segment,  
    PT_ProductId as product_id,
    PM_ProductItemId as product_item_id,
    PT_ProductDescription as product, 
    PT_ClassificationLevel3Description AS product_class, 
    PT_ClassificationLevel5Description AS product_group, 
    PT_GenealogyLevel3Description as brand, 
    PT_GenealogyLevel5Description as brewer, 
    SS_Weight as weight,
    sum(BI_ValM) as value,
    sum(BI_VolHL) as volume
from GB_BI_DATA_LIVE.dbo.vw_BI_CGA_A
where D_DateKey >= '2022-01-01 00:00:00.000'
    and D_DateKey  < '2024-01-01 00:00:00.000'
    and PT_ClassificationLevel5Description in (N'Total Beer', N'Total Cider')  
    and OT_CGAIdent > 0 
    and PT_ProductId > 0 
    and PT_AT_Format = N'Draught' 
    and CountryLevel4Description = N'GB'  
    and BI_ValM > 0 
    and BI_VolHL > 0 
group by D_DateKey, 
    D_Period,
    OT_CGAIdent,
    BARBLevel2Description, 
    OT_SegmentationLevel1Description,  
    PT_ProductId,
    PM_ProductItemId,
    PT_ProductDescription, 
    PT_ClassificationLevel3Description, 
    PT_ClassificationLevel5Description, 
    PT_GenealogyLevel3Description, 
    PT_GenealogyLevel5Description, 
    SS_Weight; 

"""

# Pull data using pandas

df_sql_query = pd.read_sql(sql_query, engine)

# LAD - long alcoholic drink.  E.g. beer, cider, Smirnoff Ice, Hooch, etc..
# Volume created in EPOS.  Get quantity and calculate it.  Be careful with cocktails - measures unknown.