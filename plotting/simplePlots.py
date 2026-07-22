import geopandas         as gpd 
import matplotlib.pyplot as plt

## First we need to process the data from the csv so we will import then take the cols that we need


merged_gdf = gpd.read_file("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedLoanData/output.GeoJSON")


#========== LEGACY CODE TO CREATE GEOJSON ================#
#tract_averages = pd.read_csv(file_name)

#local_path = "/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ShapeData/nhgis0001_shapefile_tl2000_us_tract_2000.zip"
#tract_gdf = gpd.read_file(local_path, layer="US_tract_2000")

## Filter out Alaska (020) and Hawaii (150) 
## This is because idk how to make a map with islands... (im not lazy)
## -- changed to use substring instead of querying bc 2010 uses different schema than 2000 
#state_codes = tract_gdf["GISJOIN"].str[1:4]

#continental_gdf = tract_gdf[
#    (~state_codes.isin(["020", "150"])) & (state_codes.astype(int) <= 560)
#]


## Merge on GISJOIN so the spacial data (continental_gdf) and the loan data (tract_averages) are in the same GDF 
#merged_gdf = continental_gdf.merge(tract_averages, on="GISJOIN", how="left")

## fix coordinate system, epsg is 5070 bc/ Albers Equal Area projection using meters
#merged_gdf = merged_gdf.to_crs(epsg=5070)
#merged_gdf.to_file("output.GeoJSON")
##############################################################################

## I had error where the colors did not work because some areas were over saturating the scale
print(merged_gdf["pct_subprime"].describe())

vmin_val = merged_gdf["pct_subprime"].quantile(0.01)
vmax_val = merged_gdf["pct_subprime"].quantile(0.99)


## Plot for subprime distribution (its fairly normal mean about 0.1 ish)
#sns.displot(merged_gdf["pct_subprime"], kind="kde", fill=True)
#plt.show()

merged_gdf.plot.scatter(
    x='pct_subprime',
    y='average_income',
    color='blue',
    alpha=0.6,
    figsize=(8, 6)
)
plt.title("Subprime Loan Percentage vs Average Income")
plt.xlabel("Subprime Percentage")
plt.ylabel("Average Income")
plt.show()


## set fig size and stuff
fig, ax = plt.subplots(1, 1, figsize=(20, 12))

## Plotting with explicit vmin and zmax parameters so it does not over saturate
merged_gdf.plot(
    column="pct_subprime", ## this is the thing we are plotting 
    cmap="plasma",            ## this is just color type, i like how it looks
    linewidth=0,              ## if you include tract borders you start to get the map too busy
    edgecolor="none",         ## same thing 
    legend=True,              ## just for scale 
    ax=ax,                    ## clearly
    vmin=vmin_val,            ## again with the saturation
    vmax=vmax_val,            ## see above
    missing_kwds={
        "color": "darkgrey",  # Color for tracts with NaN values
        "label": "No Data"  
    },
    legend_kwds={
        "label": "Percentage of Loans Classified as Subprime",
        "orientation": "horizontal", ## fits better
        "pad": 0.05,
        "shrink": 0.7,
        "extend": "both"  ## because we capped at 90% max there are higher values so it should be arrow
    }
)

## just a bunch of basic things on display stuff
ax.set_title("Percentage of Loans Classified as Subprime by US Census Tract", fontsize=16, fontweight="bold")
ax.axis("off")


plt.tight_layout()
plt.show()

