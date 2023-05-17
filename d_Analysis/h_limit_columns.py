from d_shares import bs
from e_rate_of_sale import ros
from f_nda_shares import nda
from g_distribution_footprint import dp

print("\n the head of bs is: \n", bs.head(2))
print("\n the head of ros is: \n", ros.head(2))
print("\n the head of nda is: \n", nda.head(2))
print("\n the head of dp is: \n", dp.head(2))


bs = bs[["date", "market", "product", "drink_group", "value_share", "volume_share"]]
ros = ros[["date", "market", "product", "drink_group", "value_ros", "volume_ros", "nda_outlet_count", "nda_data_partner"]]
dp = dp[["date", "market", "product", "drink_group", "dist_pen"]]

import pandas as pd

results = pd.merge(
    bs, ros,
    left_on=["date", "market", "product", "drink_group"],
    right_on=["date", "market", "product", "drink_group"],
    how="inner"
)

results = pd.merge(
    results, nda,
    left_on=["date", "market", "product", "drink_group"],
    right_on=["date", "market", "product", "drink_group"],
    how="inner"
)

results = pd.merge(
    results, dp,
    left_on=["date", "market", "product", "drink_group"],
    right_on=["date", "market", "product", "drink_group"],
    how="inner"
)

# rearrange order of columns

results = results[[
    "date", "market", "product", "drink_group", "value_share", "volume_share", "value_ros", "volume_ros",
    "dist_pen", "nda_outlet_count", "nda_data_partner", "nda_max_data_partner_share", "nda_data_partner_with_max_share"
]]

print(results.head(2))

