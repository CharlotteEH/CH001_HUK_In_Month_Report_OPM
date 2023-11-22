import pandas as pd

from b_review_the_data import df

df = df[df["custom_product_group"].isin(["Premium Lager", "Classic Lager", "Mainstream Lager", "Craft Ale", "Classic Ale", "Stout", "Apple Cider", "Flavoured Cider"])].copy()
df["brewer_group"] = "Group Brewer | " + df["product_group"]
#df["brand_group"] = "Group Brand | " + df["custom_product_group"]
df["drink_group"] = "Group Product | " + df["custom_product_group"]

print(df.head(2))
df_brewer = df[["date", "outlet_id", "region", "segment", "location",  "brewer", "value", "volume", "weight",
                "country", "brewer_group"]]
df_brewer = df_brewer.rename(columns={
    "brewer": "product",
    "brewer_group": "drink_group"
})
print(df_brewer.head(20))
#
# df_brand = df[["date", "outlet_id", "region", "segment", "location",  "brand", "value", "volume","weight",
#                "country", "brand_group"]]
# df_brand = df_brand.rename(columns={
#     "brand": "product",
#     "brand_group": "drink_group"
# })

df_product = df[["date", "outlet_id", "region", "segment", "location","product", "value", "volume","weight",
                "country", "drink_group"]]
df_product = df_product.rename(columns={
    "product": "product",
    "drink_group": "drink_group"
})

df = pd.concat(
    [
        df_brewer,  df_product  # df_brand,
    ], axis=0
)


region = df[[
    "date", "outlet_id", "region",  "product", "drink_group", "value", "volume","weight"
]]
region = region.rename(columns={"region":"market"})

region["market_group"] = "Region"

segment = df[[
    "date", "outlet_id", "segment", "product", "drink_group", "value", "volume", "weight"
]]
segment = segment.rename(columns={"segment":"market"})

segment["market_group"] = "Segment"

location = df[[
    "date", "outlet_id", "location",  "product", "drink_group", "value", "volume", "weight"
]]
location = location.rename(columns={"location":"market"})

location["market_group"] = "Location"

country = df[[
    "date", "outlet_id", "country",  "product", "drink_group", "value", "volume", "weight"
]]
country = country.rename(columns={"country":"market"})

country["market_group"] = "Country"

df = pd.concat([region, segment, location, country], axis=0)


df["market"] = df["market_group"]+" | " + df["market"]
# from pathlib import Path
#
# cwd = Path(__file__).parent
#
# df.to_csv(cwd / "test.csv", index=False)