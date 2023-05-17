from f_nda_shares import df
import pandas as pd

bd = df.groupby(
    [
        "date", "market", "product", "drink_group"
    ]
).agg(
    {
        "outlet_id":pd.Series.nunique
    }
)

bd.columns = bd.columns.get_level_values(0)
bd = bd.reset_index()
bd = bd.rename(columns={"outlet_id":"product_dist"})

td = df.groupby(
    [
        "date", "market"
    ]
).agg(
    {
        "outlet_id":pd.Series.nunique
    }
)

td.columns = td.columns.get_level_values(0)
td = td.reset_index()
td = td.rename(columns={"outlet_id":"total_dist"})

print(bd.head(2))
print(td.head(2))

# distribution penetration

dp = pd.merge(
    bd, td,
    left_on=["date", "market"],
    right_on=["date", "market"],
    how="inner"
)

dp["dist_pen"] = dp["product_dist"]/dp["total_dist"]

print(dp.head(20))

