import polars as pl 


df1 = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/ACS_5YR_ESTIMATES_HOUSING_TRACT_-6586867065303880862.csv", infer_schema_length=10000000000)


df2 = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/ACS_5YR_ESTIMATES_SOCIOECONOMIC_TRACT_-4830078498712968728.csv", infer_schema_length=10000000000)


merged_df = df1.join(df2, on="TRACT", how="inner")

merged_df.write_csv("merged_housing.csv")
