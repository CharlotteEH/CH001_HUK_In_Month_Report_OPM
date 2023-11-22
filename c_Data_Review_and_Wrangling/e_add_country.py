# add GB column

from d_remove_outliers import df
import pandas as pd

df["country"] = "GB"

# add total 4 week date for brewer

#df["date"] = df["date"].astype(str)

# all = df[:]
# all["date"] = "4 week period"
# df = pd.concat([df, all])

# df["report_period"] = df["period"] - 208
# all = df[:]
# all["date"] = "Four Week Period" + " " + all["report_period"].astype(str)
# df = pd.concat([df, all])
#
# print(df.head())
# print(df.tail())