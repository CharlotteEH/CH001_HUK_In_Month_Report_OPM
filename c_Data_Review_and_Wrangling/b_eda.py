import pandas as pd

from a_read_in_the_data import df, cider_flavours

print("\nthe head of df is:\n", df.head(5), "\n")
print("\nthe head of cider_flavours is:\n", cider_flavours.head(5), "\n")

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

# check the product segment
u = df["product_segment"].unique()
print("\nthe unique product segments are:\n", sorted(u),"\n")

# # check the cil segment
# u = df["cil_segment"].unique()
# print("\nthe unique cil segments are:\n", sorted(u),"\n")

# check the product class
u = df["product_class"].unique()
print("\nthe unique product classes are:\n", sorted(u),"\n")

# check the product groups
u = df["product_group"].unique()
print("\nthe unique product groups are:\n", sorted(u),"\n")

cider_flavours = cider_flavours[["product_id", "cider_flavour"]]

df = pd.merge(
    df, cider_flavours,
    left_on=["product_id"],
    right_on=["product_id"],
    how="left"
)

u = cider_flavours["cider_flavour"].unique()
print("\nthe unique cider flavours are:\n", sorted(u),"\n")

print(df.head(20))