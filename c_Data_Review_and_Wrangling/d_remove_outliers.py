import pandas as pd
import numpy as np

from c_update_product_group import df

print("\nthe shape of df before removing outliers is:\n", df.shape)

# aggregate the columns required
ag = df.groupby(
    [
        "date",
        "outlet_id"
    ]
).agg(
    {
        "value": ["sum"]
    }
)
ag.columns = ag.columns.get_level_values(0) # 0 is for first row

ag = ag.reset_index()

# mean and standard deviations

msd = ag.groupby(
    [
        "date"
    ]
).agg(
    {
        "value": ["mean", np.std],
        "outlet_id": pd.Series.nunique
    }
)
msd.columns = msd.columns.map("|".join).str.strip("|")

msd = msd.reset_index()

msd = msd.rename(
    columns={
        "outlet_id|nunique": "outlet_id|count"
    }
)

# remove low outlet counts due to standard deviations

msd = msd.loc[msd["outlet_id|count"]>1]

msd = msd[["date","value|mean","value|std"]]

# merge and calculate z scores

z = pd.merge(
    ag, msd,
    left_on=["date"],
    right_on=["date"],
    how="inner"
)

z["z_score"] = (z["value"]-z["value|mean"]) / z["value|std"]
z["z_score"] = z["z_score"].abs()

# take the acceptable rows

z = z.loc[z["z_score"]<3]

# take the columns required for merging

z = z[["date", "outlet_id"]]

# merge the acceptable rows with the data

df = pd.merge(
    df, z,
    left_on=["date", "outlet_id"],
    right_on=["date", "outlet_id"],
    how="inner"
)

print("\nthe shape of df after removing outliers is:\n", df.shape)

