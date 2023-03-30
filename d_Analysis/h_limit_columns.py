from d_shares import bs
from e_rate_of_sale import ros
from f_nda_shares import nda
from g_distribution_footprint import dp

print("\n the head of bs is: \n", bs.head(2))
print("\n the head of ros is: \n", ros.head(2))
print("\n the head of nda is: \n", nda.head(2))
print("\n the head of dp is: \n", dp.head(2))


bs = bs[["date", "market", "product", "product_group", "value_share", "volume_share"]]
ros = ros[["date", "market", "product", "product_group", "value_ros", "volume_ros", "nda_outlet_count", "nda_data_partner"]]
dp = dp[["date", "market", "product", "product_group", "dist_pen"]]

import pandas as pd

results = pd.merge(
    bs, ros,
    left_on=["date", "market", "product", "product_group"],
    right_on=["date", "market", "product", "product_group"],
    how="inner"
)

results = pd.merge(
    results, nda,
    left_on=["date", "market", "product", "product_group"],
    right_on=["date", "market", "product", "product_group"],
    how="inner"
)

results = pd.merge(
    results, dp,
    left_on=["date", "market", "product", "product_group"],
    right_on=["date", "market", "product", "product_group"],
    how="inner"
)

print(results.head(2))

