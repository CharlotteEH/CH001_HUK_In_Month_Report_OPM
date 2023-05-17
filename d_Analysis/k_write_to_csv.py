from j_extract_lists import  list_date, list_market, list_product
from i_apply_ndas import wide_results
from pathlib import Path

cwd = Path(__file__).parent

list_date.to_csv(cwd / "list_date.csv", index=False)
list_market.to_csv(cwd / "list_market.csv", index=False)
list_product.to_csv(cwd / "list_product.csv", index=False)

wide_results.to_csv(cwd / "wide_results.csv", index=False)