from c_append_data import df
from pathlib import Path

import pandas as pd

# ros for the product level
ros_product = df.groupby(
    [
        "date", "market", "outlet_id", "product",  "weight"
    ]
).agg(
    {
        "value": "sum",
        "volume": "sum"
    }
)
ros_product.columns = ros_product.columns.get_level_values(0)
ros_product = ros_product.reset_index()

print(ros_product.head(2))

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
ros_drink_group = ros_drink_group.rename(columns={"drink_group":"product"})

ros = pd.concat([ros_product, ros_drink_group], axis=0)

ros = ros.groupby(
    [
        "date", "market", "product"
    ]
).agg(
    {
        "weight": "sum",
        "value": "sum",
        "volume": "sum"
    }
)
ros.columns = ros.columns.get_level_values(0)
ros = ros.reset_index()

print(ros.head(10))
print(ros.tail())

from pathlib import Path

path = Path("Z:/PycharmProjects/CH001_HUK_In_Month_Report_OPM/d_Analysis")

ros.to_csv(path / "disttest.csv", index=False)