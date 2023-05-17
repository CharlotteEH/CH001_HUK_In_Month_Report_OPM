from f_convert_volumes import df

from pathlib import Path

cwd = Path(__file__).parent

df.to_csv(cwd / "data_cleaned.csv", index=False)