import polars as pl
import sys

file_1      = sys.argv[1]
file_2      = sys.argv[2]
output_file = sys.argv[3]


print("-" * 20)
print("collecting rest of data")

df   = pl.read_csv(file_1, infer_schema_length=100000000)
df_2 = pl.read_csv(file_2, infer_schema_length=100000000)

df_3 = df.join(df_2, on="GEOID", how="inner")

df_reduced = df_3.select(
    (pl.lit("G")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(0, 2)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(2, 3)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(5, 6)
    ).alias("GISJOIN"),


    ((
        pl.col("B25014_MODCROWD_O")
        + pl.col("B25014_SEVCROWD_O")
        + pl.col("B25014_MODCROWD_R")
        + pl.col("B25014_SEVCROWD_R")
    )   / pl.col("B25002EST1")
    ).alias("Overcrowding_Rate"),

   pl.col("B25106_CB_GT35_PCT").alias("Cost_Burden_PCT"),

   pl.col("B23001_UE_PCT").alias("Unemployment_PCT"),

   pl.col("B17021EST2_PCT").alias("Poverty_Rate_PCT"),

   pl.col("B19013EST1").alias("Median_Household_Income")
)

df_reduced.write_csv(output_file)
print("collected rest of data")
