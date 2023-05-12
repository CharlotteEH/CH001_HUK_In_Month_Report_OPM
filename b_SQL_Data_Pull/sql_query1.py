# sql_query.py ---------------------------------------------------------------

""" Query to pull data
Note that will also work with the pound sign in the value column"""

import pandas as pd

from connection import engine

sql_query = f"""
select distinct h.D_DateKey as date,  -- The date column to use
    h.OT_CGAIdent as outlet_id,  -- The outlet unique number
       o.OT_TL2_Novellus as region,  -- The regions of the country to use
       h.OT_SL1 as segment,  -- The segments of the outlet, for example; bar, restaurant
       h.OT_LocationDescription as location,  -- What part of area it is in, for example; high street, city centre
       h.PI_ClientDescription as data_partner, -- The data partner that supplied the data
       h.PT_ProductDescription as product,  -- Product level data
       h.PT_AT_HUK_Segment AS product_segment, 
       h.PT_AT_Cil_Segment AS cil_segment,
       h.PT_CL3_CGA AS product_class, -- e.g. premium cider, standard lager
       h.PT_CL5_CGA AS product_group, -- beer or cider
       h.PT_GL3_CGA as brand,  -- Product brand
       h.PT_GL5_CGA as brewer,  -- The company who own and brew the product (not the supplier or distributor, be warned: CS often call the brewer "supplier")
    sum(h.[F_SalesValue_£]) as value,  -- The money paid by the consumer
       sum(h.F_SalesVolume_MLS) as volume  -- The volume in MLS
from WS_LIVE.dbo.vw_Epos_HUK_Weekly as h  -- The Heineken database to use for HUK EPOS projects.  HUK data that is not shared with others.  + customer segmentation.
    inner join OI_LIVE.dbo.vw_Outlet as o  -- We had to join on this to get the newer Novellus / BARB outlet segmentation since they are not in the HUK databases
           on h.OT_CGAIdent = o.OT_CGAIdent  -- The column we joined
where h.D_DateId >= 20230101  -- The earliest date to use, we use this column for date predicates because it's the primary key, and operates faster.  OPM: on premise model.
    and h.PT_CL5_CGA in (N'Total Beer', N'Total Cider')  -- Limit to beer and cider, PT_CL5_CGA has these
       and h.OT_CGAIdent > 0  -- Remove unwanted outlets
       and h.PT_ProductId > 0  -- Remove unwanted products
       and h.PT_AT_Format = N'Draught'  -- Limit to draught
       and h.OT_TL5_ISBA = N'GB'  -- Remove offshore outlets
       and h.[F_SalesValue_£] > 0  -- Just in case of, and good practice
       and h.F_SalesVolume_MLS > 0  -- Just in case of, and good practice
group by h.D_DateKey,
    h.OT_CGAIdent,
       o.OT_TL2_Novellus,
       h.OT_SL1,
       h.OT_LocationDescription,
       h.PI_ClientDescription,
       h.PT_ProductDescription,
       h.PT_AT_HUK_Segment,
       h.PT_AT_Cil_Segment,
       h.PT_CL3_CGA,
       h.PT_CL5_CGA,
       h.PT_GL3_CGA,
       h.PT_GL5_CGA;

"""

# Pull data using pandas

df_sql_query = pd.read_sql(sql_query, engine)

# LAD - long alcoholic drink.  E.g. beer, cider, Smirnoff Ice, Hooch, etc..
# Volume created in EPOS.  Get quantity and calculate it.  Be careful with cocktails - measures unknown.