from d_add_country import df

from pathlib import Path

cwd = Path(__file__).parent

df.to_csv(cwd / "data_cleaned.csv", index=False)