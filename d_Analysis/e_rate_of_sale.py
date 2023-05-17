from d_shares import df

import pandas as pd

ros = df.groupby(
    [
        "date", "market", "product", "drink_group"
    ]
).agg(
    {
        "value": ["sum"],
        "volume": ["sum"],
        "outlet_id": pd.Series.nunique,
        "data_partner": pd.Series.nunique
    }
)
# 50 outlets, 3 data partners, less than 50% per partner

print(ros.head(2))


ros.columns = ros.columns.get_level_values(0)
ros = ros.reset_index()
ros = ros.rename(columns={"outlet_id":"nda_outlet_count",
                          "data_partner":"nda_data_partner"})

ros["value_ros"] = ros["value"]/ros["nda_outlet_count"]
ros["volume_ros"] = ros["volume"]/ros["nda_outlet_count"]

print(ros.head(15))
