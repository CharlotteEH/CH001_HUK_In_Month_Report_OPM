import pandas as pd

from b_review_the_data import df

region = df[[
    "date", "outlet_id", "region", "data_partner", "brewer", "value", "volume"
]]
region = region.rename(columns={"region":"market"})

segment = df[[
    "date", "outlet_id", "segment", "data_partner", "brewer", "value", "volume"
]]
segment = segment.rename(columns={"segment":"market"})

location = df[[
    "date", "outlet_id", "location", "data_partner", "brewer", "value", "volume"
]]
location = location.rename(columns={"location":"market"})

country = df[[
    "date", "outlet_id", "country", "data_partner", "brewer", "value", "volume"
]]
country = country.rename(columns={"country":"market"})


df = pd.concat([region, segment, location, country], axis=0)

