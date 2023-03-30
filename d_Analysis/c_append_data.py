import pandas as pd

from b_review_the_data import df
df["brewer_group"] = "Group Brewer | " + df["product_class"]
df["brand_group"] = "Group Brand | " + df["product_class"]

print(df.head(2))
df_brewer = df[["date", "outlet_id", "region", "segment", "location", "data_partner", "brewer", "value", "volume", "country", "brewer_group"]]
df_brewer = df_brewer.rename(columns={
    "brewer": "product",
    "brewer_group": "product_group"
})

df_brand = df[["date", "outlet_id", "region", "segment", "location", "data_partner", "brand", "value", "volume", "country", "brand_group"]]
df_brand = df_brand.rename(columns={
    "brand": "product",
    "brand_group": "product_group"
})
df = pd.concat(
    [
        df_brewer, df_brand
    ], axis=0
)


print(df_brewer.head(2))
print(df_brand.head(2))

region = df[[
    "date", "outlet_id", "region", "data_partner", "product", "product_group", "value", "volume"
]]
region = region.rename(columns={"region":"market"})

region["market_group"] = "Region"

segment = df[[
    "date", "outlet_id", "segment", "data_partner", "product", "product_group", "value", "volume"
]]
segment = segment.rename(columns={"segment":"market"})

segment["market_group"] = "Segment"

location = df[[
    "date", "outlet_id", "location", "data_partner", "product", "product_group", "value", "volume"
]]
location = location.rename(columns={"location":"market"})

location["market_group"] = "Location"

country = df[[
    "date", "outlet_id", "country", "data_partner", "product", "product_group", "value", "volume"
]]
country = country.rename(columns={"country":"market"})

country["market_group"] = "Country"

df = pd.concat([region, segment, location, country], axis=0)


df["market"] = df["market_group"]+" | " + df["market"]
