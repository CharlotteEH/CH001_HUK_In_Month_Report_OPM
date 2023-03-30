from h_limit_columns import results

from pathlib import Path

cwd = Path(__file__).parent

results.to_csv(cwd / "results.csv", index=False)