from h_limit_columns import results

print(results.head())

results = results.loc[
(results["nda_outlet_count"] >= 50) &
(results["nda_data_partner"] >= 3) &
(results["nda_max_data_partner_share"] <= 0.5)
]

results = results[["date", "market", "product", "product_group", "value_share", "volume_share", "value_ros"
                   , "volume_ros", "dist_pen"]]