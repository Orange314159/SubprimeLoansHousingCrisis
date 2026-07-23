from numpy import trace
import polars as pl 
import polars.datatypes as pld
import sys 
## First we need to process the data from the csv so we will import then take the cols that we need


input_file  = sys.argv[1]
output_file = sys.argv[2]
file_number = int(sys.argv[3])

schema_early = {
    'year': pl.Int64, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 'loan_amount': pl.String, 
    'census_tract': pl.String, 'income': pl.String, 'applicant_race': pl.Int64, 'state_code': pl.String, 
    'county_code': pl.String
}

schema_middle = {
   'year': pl.Int64, 'loan_type': pl.Int64, 'census_tract': pl.String, 'income': pl.String, 
   'applicant_race': pl.Int64, 'rate_spread': pl.Float64, 'hoepa_status': pl.Int64, 'loan_amount': pl.Int64, 
   'state_code': pl.String, 'county_code': pl.Int64 
}

schema_late = {
    'year': pl.Int64, 'loan_type': pl.Int64, 'census_tract': pl.String, 'income': pl.Int64, 
    'applicant_race': pl.Int64, 'rate_spread': pl.Float64, 'hoepa_status': pl.Int64, 'loan_amount': pl.Int64, 
    'state_code': pl.String, 'county_code': pl.String
}

print("-" * 20)
print(f"Reducing {input_file}")

if file_number > 2003:
    ## Middle (2004 - 2006)
    df = pl.read_csv(input_file, schema=schema_middle)
elif file_number > 2006:
    ## Late (2007 - 2010)
    df = pl.read_csv(input_file, schema=schema_late)
else:
    ## Early (2000 - 2003)
    df = pl.read_csv(input_file, schema=schema_early)



## Process the HMDA data to construct a matching NHGIS GISJOIN string
df_processed = (df.with_columns([
    pl.col("income").cast(pl.Int64, strict=False),
    pl.col("rate_spread").fill_null(0).cast(pl.Float64, strict=False), 
    pl.col("state_code").cast(pl.String).str.zfill(2),
    pl.col("county_code").cast(pl.String).str.zfill(3),
    pl.col("census_tract").str.split(".")
    .map_elements(lambda x: f"{x[0].zfill(4)}{x[1].ljust(2, '0')}" if len(x) == 2 else f"{x[0].zfill(4)}00", return_dtype=pl.String).alias("cleaned_tract")## This line was given to me by Gemini because I could not figure out how to adjust the formats between the tracts 
]).filter(pl.col("income").is_not_null()))

## now split into 0 and 1 for rate spread
df_processed_2 = df_processed.with_columns(
    pl.col("rate_spread").ne(0).cast(pl.Int32)
)


## NHGIS format for 2000 tracts they are in a format like G_SATE_COUNTY_TRACT
df_final = df_processed_2.with_columns((
        pl.lit("G") 
        + pl.col("state_code") 
        + pl.lit("0") 
        + pl.col("county_code") 
        + pl.lit("0") 
        + pl.col("cleaned_tract")
    ).alias("GISJOIN")
)

tract_averages = (
    df_final
    .group_by("GISJOIN")                         ## All of the records in the same tract should be averaged
    .agg(
        pl.col("rate_spread").mean().alias("pct_subprime"),
        pl.col("income").mean().alias("average_income"),
        pl.len().alias("weight")
    ) ## We are concerned with the aggregate average

).to_pandas() ## finally we need this in a pandas data frame because we are using geopandas


tract_averages.to_csv(output_file)

print(f"finished reducing {output_file}")
