import pandas as pd

from c_append_data import df

# brewer share
bs = df.groupby(
    [
        "date", "market", "brewer"
    ]
).agg(
    {
        "value": ["sum"],
        "volume": ["sum"]
    }
)
bs.columns = bs.columns.get_level_values(0)
bs = bs.reset_index()

# total share
ts = bs.groupby(
    [
        "date", "market"
    ]
).agg(
    {
        "value": ["sum"],
        "volume": ["sum"]
    }
)

ts.columns = ts.columns.get_level_values(0)
ts = ts.reset_index()

ts = ts.rename(columns={"value":"total_value", "volume":"total_volume"})


bs = pd.merge(
    bs, ts,
    left_on=["date", "market"],
    right_on=["date", "market"],
    how="inner"
)

bs["value_share"]=bs["value"]/bs["total_value"]
bs["volume_share"]=bs["volume"]/bs["total_volume"]



print(bs.head(2))
