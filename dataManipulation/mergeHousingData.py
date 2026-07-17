import polars as pl

drop_cols = [ ## cols that are in both data sets don't need to exist twice in the final data set
    "OBJECTID", "STATE", "COUNTY", "TRACT", "NAME", "CNTY_FIPS", 
    "EACODE", "EANAME", "Shape__Area", "Shape__Length"
]

housing_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/ACS_5YR_ESTIMATES_HOUSING_TRACT_-6586867065303880862.csv", schema_overrides={"GEOID": pl.String}, infer_schema_length=1000000)

socio_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/ACS_5YR_ESTIMATES_SOCIOECONOMIC_TRACT_-4830078498712968728.csv", schema_overrides={"GEOID": pl.String}, infer_schema_length=1000000)

socio_subset = socio_data.drop(drop_cols) ## remove those cols !!


merged_df = housing_data.join(socio_subset, "GEOID", how="inner")

print(merged_df.height)

merged_df.write_csv("clean_merged_data.csv")
