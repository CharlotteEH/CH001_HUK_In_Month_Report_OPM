from h_limit_columns import results
# from pathlib import Path
#
# cwd = Path(__file__).parent
#
# results.to_csv(cwd / "nda_test.csv", index=False)
print(results.head())

results = results.loc[
(results["nda_outlet_count"] >= 50) &
(results["nda_data_partner"] >= 3) &
(results["nda_max_data_partner_share"] <= 0.5)
]

results = results[["date", "market", "product", "drink_group", "value_share", "volume_share", "value_ros"
                   , "volume_ros", "dist_pen", "nda_outlet_count",	"nda_data_partner",
                   "nda_max_data_partner_share",	"nda_data_partner_with_max_share"]]

import pandas as pd

columns_to_widen = ["value_share", "volume_share", "value_ros", "volume_ros", "dist_pen"]

wide_results = pd.melt(results, id_vars=["date", "market", "product", "drink_group"], value_vars=columns_to_widen, var_name="fact", value_name="value")

