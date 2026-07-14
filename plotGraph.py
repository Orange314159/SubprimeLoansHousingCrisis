import polars as pl 
import geopandas as gpd 
import matplotlib.pyplot as plt 

## First we need to process the data from the csv so we will import then take the cols that we need

schema_2000 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy_type': pl.Int64, 'loan_amount': pl.String, 'action_taken': pl.Int64, 
    'msamd': pl.String, 'state_code': pl.String, 'county_code': pl.String, 'census_tract': pl.String, 
    'applicant_race_1': pl.Int64, 'co_applicant_race_1': pl.Int64, 'applicant_sex': pl.Int64, 
    'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 'denial_reason_1': pl.Int64, 
    'denial_reason_2': pl.Int64, 'denial_reason_3': pl.Int64, 'edit_status': pl.Int64, 
    'sequence_number': pl.Int64
}

file_number = 2000
file_name = f"/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/LoanData/HMDA_DATA_SET/HMDA_{file_number}/HMDA_{file_number}.csv"

df = pl.read_csv(file_name, schema=schema_2000)

## Process the HMDA data to construct a matching NHGIS GISJOIN string
df_processed = df.with_columns([
    pl.col("loan_amount").cast(pl.Float64, strict=False),
    pl.col("state_code").str.zfill(2),
    pl.col("county_code").str.zfill(3),
    pl.col("census_tract").str.split(".")
    .map_elements(lambda x: f"{x[0].zfill(4)}{x[1].ljust(2, '0')}" if len(x) == 2 else f"{x[0].zfill(4)}00", return_dtype=pl.String).alias("cleaned_tract")## This line was given to me by Gemini because I could not figure out how to adjust the formats between the tracts 
])

## NHGIS format for 2000 tracts they are in a format like G_SATE_COUNTY_TRACT
df_final = df_processed.with_columns((
        pl.lit("G") 
        + pl.col("state_code") 
        + pl.lit("0") 
        + pl.col("county_code") 
        + pl.lit("0") 
        + pl.col("cleaned_tract")
    ).alias("GISJOIN")
)


## Aggregate loan amounts by GISJOIN identifier
tract_averages = (
    df_final
    .filter(pl.col("loan_amount").is_not_null()) ## We actually need data we can't just guess
    .group_by("GISJOIN")                         ## All of the records in the same tract should be averaged
    .agg(pl.col("loan_amount").mean().alias("avg_loan_amount")) ## We are concerned with the aggregate average 
).to_pandas() ## finally we need this in a pandas data frame because we are using geopandas


## Now onto actually drawing the graph
local_path = "/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ShapeData/nhgis0001_shapefile_tl2000_us_tract_2000.zip"
tract_gdf = gpd.read_file(local_path, layer="US_tract_2000")

## Filter out Alaska (020) and Hawaii (150) 
## This is because idk how to make a map with islands... (im not lazy)
continental_gdf = tract_gdf[
    (~tract_gdf["NHGISST"].isin(["020", "150"])) & (tract_gdf["NHGISST"].astype(int) <= 560)
]

## Merge on GISJOIN so the spacial data (continental_gdf) and the loan data (tract_averages) are in the same GDF 
merged_gdf = continental_gdf.merge(tract_averages, on="GISJOIN", how="inner")

## fix cordinate system, epsg is 5070 bc/ Albers Equal Area projection using meters
merged_gdf = merged_gdf.to_crs(epsg=5070)


## I had error where the colors did not work because some areas were oversaturating the scale
print(merged_gdf["avg_loan_amount"].describe())

vmin_val = merged_gdf["avg_loan_amount"].quantile(0.1)
vmax_val = merged_gdf["avg_loan_amount"].quantile(0.9)

## set fig size and stuff
fig, ax = plt.subplots(1, 1, figsize=(20, 12))

## Plotting with explicit vmin and vmax parameters so it does not oversaturate
merged_gdf.plot(
    column="avg_loan_amount", ## this is the thing we are plotting 
    cmap="plasma",            ## this is just color type, i like how it looks
    linewidth=0,              ## if you include tract borders you start to get the map too busy
    edgecolor="none",         ## same thing 
    legend=True,              ## just for scale 
    ax=ax,                    ## clearly
    vmin=vmin_val,            ## again with the saturation
    vmax=vmax_val,            ## see above
    legend_kwds={
        "label": "Average Loan Amount (Thousands of Dollars)",
        "orientation": "horizontal", ## fits better
        "pad": 0.05,
        "shrink": 0.7,
        "extend": "max"  ## because we capped at 90% max there are higher values so it should be arrow
    }
)

## just a bunch of basic things on display stuff
ax.set_title("Average Loan Amount by US Census Tract (Continental USA - Year 2000 Data)", fontsize=16, fontweight="bold")
ax.axis("off")

plt.savefig('high_res_plot.png', dpi=2200, bbox_inches='tight')
plt.tight_layout()
plt.show()

