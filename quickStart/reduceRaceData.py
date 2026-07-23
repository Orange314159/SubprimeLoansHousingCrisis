import polars as pl
import sys


input_file  = sys.argv[1]
output_file = sys.argv[2]


print("-" * 20)
print("collecting race data")

df = pl.read_csv(input_file)

df_reduced = df.select(
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

df_reduced.write_csv(output_file)

print("collected race data")
