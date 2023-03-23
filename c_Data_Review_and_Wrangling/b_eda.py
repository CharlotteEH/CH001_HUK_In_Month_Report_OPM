from a_read_in_the_data import df

print("\nthe head of df is:\n", df.head(5), "\n")

# check the dates
u = df["date"].unique()
print("\nthe unique dates are:\n", sorted(u),"\n")

# check the region
u = df["region"].unique()
print("\nthe unique regions are:\n", sorted(u),"\n")

# check the segment
u = df["segment"].unique()
print("\nthe unique segments are:\n", sorted(u),"\n")

# check the locations
u = df["location"].unique()
print("\nthe unique locations are:\n", sorted(u),"\n")