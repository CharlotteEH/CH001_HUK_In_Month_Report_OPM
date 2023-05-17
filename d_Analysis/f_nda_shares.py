from e_rate_of_sale import df

import pandas as pd
# get data partner volumes

dp_volumes = df.groupby(
    [
        "date", "market", "product", "drink_group", "data_partner"
    ]
).agg(
    {
        "volume": ["sum"]
    }
)

dp_volumes.columns = dp_volumes.columns.get_level_values(0)
dp_volumes = dp_volumes.reset_index()
dp_volumes = dp_volumes.rename(columns={"volume":"dp_volume"})

# get total volumes

total_volumes = dp_volumes.groupby(
    [
        "date", "market", "product", "drink_group"
    ]
).agg(
    {
        "dp_volume": ["sum"]
    }
)

total_volumes.columns = total_volumes.columns.get_level_values(0)
total_volumes = total_volumes.reset_index()

total_volumes = total_volumes.rename(columns={"dp_volume":"total_volume"})

nda = pd.merge(
    dp_volumes, total_volumes,
    left_on= ["date", "market", "product", "drink_group"],
    right_on= ["date", "market", "product", "drink_group"],
    how="inner"
)
# total volume for market on that day

# data partner share

nda["dp_volume_share"] = nda["dp_volume"]/nda["total_volume"]

nda["rank"] = nda.groupby(
    [
        "date", "market", "product", "drink_group"
    ])["dp_volume_share"].rank(ascending=False)

nda = nda.loc[nda["rank"]==1]

nda = nda.rename(columns={"data_partner":"nda_data_partner_with_max_share",
                          "dp_volume_share":"nda_max_data_partner_share"})

nda = nda[["date", "market", "product", "drink_group", "nda_max_data_partner_share", "nda_data_partner_with_max_share"]]

print(nda.head(2))

# next thing is: distribution footprint and brands

