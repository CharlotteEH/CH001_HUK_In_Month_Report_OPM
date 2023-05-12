from j_extract_lists import results, list_date, list_market, list_product
from pathlib import Path

cwd = Path(__file__).parent

list_date.to_csv(cwd / "list_date.csv", index=False)
list_market.to_csv(cwd / "list_market.csv", index=False)
list_product.to_csv(cwd / "list_product.csv", index=False)

results.to_csv(cwd / "results.csv", index=False)