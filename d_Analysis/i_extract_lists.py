from h_limit_columns import  results

print("\nThe available columns in the results are:\n")
print(results.columns)

list_date = results[["date"]]
list_date = list_date.drop_duplicates()
list_date = list_date.sort_values(by=["date"])

list_market = results[["market"]]
list_market = list_market.drop_duplicates()
list_market = list_market.sort_values(by=["market"])

list_product = results[["product", "product_group"]]
list_product = list_product.drop_duplicates()
list_product = list_product.sort_values(by=["product_group", "product"])

