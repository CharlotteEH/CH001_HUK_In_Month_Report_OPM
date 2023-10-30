from f_convert_volumes import df

from pathlib import Path

path = Path("Z:/PycharmProjects/CH001_HUK_In_Month_Report_1/c_Data_Review_and_Wrangling")

df.to_csv(path / "data_cleaned.csv", index=False)