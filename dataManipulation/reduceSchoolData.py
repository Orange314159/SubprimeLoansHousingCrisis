import polars as pl
import sys

file_name = sys.argv[1]
## df = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/ACS_5YR_ESTIMATES_SOCIOECONOMIC_TRACT_-4830078498712968728.csv")
df = pl.read_csv(f"{file_name}")


df_reduced = df.select(
    ## add the G to the beginning 
    (pl.lit("G")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(0, 2)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(2, 3)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(5, 6)
    ).alias("GISJOIN"),

    pl.col("B23006EST27_PCT").alias("undergrad_pct")
)


print(df_reduced.head(15))

df_reduced.write_csv('/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/reducedSchool.csv')
