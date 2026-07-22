import polars as pl


df = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/ACS_5YR_ESTIMATES_DEMOGRAPHIC_TRACT_-85781284450125383.csv")

df_reduced = df.select(
    ## add the G to the beginning 
    (pl.lit("G")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(0, 2)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(2, 3)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(5, 6)
    ).alias("GISJOIN"),

    pl.col("B03002EST3_PCT").alias("white_pct"),
    pl.col("B03002EST4_PCT").alias("black_pct"),
    pl.col("B03002EST12_PCT").alias("hispanic_pct")
)


print(df_reduced.head())

df_reduced.write_csv('/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/reducedRaceSchool.csv')
