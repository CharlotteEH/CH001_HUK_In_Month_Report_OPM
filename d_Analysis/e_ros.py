from d_checking_distribution import df
from pathlib import Path

path = Path("Z:/PycharmProjects/CH001_HUK_In_Month_Report_OPM/d_Analysis")


import pandas as pd


# ros for the product level
ros_product = df.groupby(
    [
        "date", "market", "outlet_id", "product", "drink_group", "weight"
    ]
).agg(
    {
        "value": "sum",
        "volume": "sum"
    }
)
ros_product.columns = ros_product.columns.get_level_values(0)
ros_product = ros_product.reset_index()

print(ros_product.head(10))

ros_product = ros_product.groupby(
    [
        "date", "market","product","drink_group"
    ]
).agg(
    {
        "weight": "sum",
        "value": "sum",
        "volume": "sum"
    }
)
ros_product.columns = ros_product.columns.get_level_values(0)
ros_product = ros_product.reset_index()

print(ros_product.head())


# ros for product group
ros_drink_group = df.groupby(
    [
        "date", "market", "outlet_id", "drink_group", "weight" # every outlet id in once for every product
    ]
).agg(
    {
        "value": "sum",
        "volume": "sum"
    }
)
ros_drink_group.columns = ros_drink_group.columns.get_level_values(0)
ros_drink_group = ros_drink_group.reset_index()

print(ros_drink_group.head(10))

ros_drink_group = ros_drink_group.groupby(
    [
        "date", "market", "drink_group"
    ]
).agg(
    {
        "weight": "sum",
        "value": "sum",
        "volume": "sum"
    }
)
ros_drink_group.columns = ros_drink_group.columns.get_level_values(0)
ros_drink_group = ros_drink_group.reset_index()
ros_drink_group = ros_drink_group.rename(columns={"weight": "group_weight",
                                                  "value": "group_value",
                                                  "volume": "group_volume"})

print(ros_drink_group.head(10))

ros = pd.merge(
    ros_product, ros_drink_group,
    on=["date", "market", "drink_group"],
    how="inner"
)

print(ros.head())

ros["volume_ros"] = ros["volume"]/ros["weight"]
ros["value_ros"] = ros["value"]/ros["weight"]

ros["volume_share"] = ros["volume"]/ros["group_volume"]
ros["value_share"] = ros["value"]/ros["group_value"]


dist = df.groupby(
    [
        "date", "market", "outlet_id", "weight"
    ]
).agg(
    {
        "value": "sum",
        "volume": "sum"
    }
)
dist.columns = dist.columns.get_level_values(0)
dist = dist.reset_index()

dist = dist.groupby(
    [
        "date", "market"
    ]
).agg(
    {
        "weight": "sum"
    }
)
dist.columns = dist.columns.get_level_values(0)
dist = dist.reset_index()
dist = dist.rename(columns={"weight": "market_weight"})


ros = pd.merge(
    ros, dist,
    on=["date", "market"],
    how="inner"
)

ros["dist_pen"] = ros["weight"]/ros["market_weight"]

# ros.to_csv(path / "rostest3.csv", index=False)

results = ros[["date", "market", "product", "drink_group", "volume_ros", "value_ros", "volume_share", "value_share",
               "dist_pen"]]

columns_to_widen = ["value_share", "volume_share", "value_ros", "volume_ros", "dist_pen"]

wide_results = pd.melt(results, id_vars=["date", "market", "product", "drink_group"], value_vars=columns_to_widen, var_name="fact", value_name="value")

