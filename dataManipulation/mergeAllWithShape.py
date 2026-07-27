import geopandas as gpd
import pandas as pd
import sys

file_name = sys.argv[1]

tract_averages = pd.read_csv(file_name)

local_path = "/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ShapeData/nhgis0001_shapefile_tl2000_us_tract_2000.zip"
tract_gdf = gpd.read_file(local_path, layer="US_tract_2000")

## Filter out Alaska (020) and Hawaii (150) 
## This is because idk how to make a map with islands... (im not lazy)
## -- changed to use substring instead of querying bc 2010 uses different schema than 2000 
state_codes = tract_gdf["GISJOIN"].str[1:4]

continental_gdf = tract_gdf[
    (~state_codes.isin(["020", "150"])) & (state_codes.astype(int) <= 560)
]


## Merge on GISJOIN so the spacial data (continental_gdf) and the loan data (tract_averages) are in the same GDF 
merged_gdf = continental_gdf.merge(tract_averages, on="GISJOIN", how="left")

## fix coordinate system, epsg is 5070 bc/ Albers Equal Area projection using meters
merged_gdf = merged_gdf.to_crs(epsg=5070)
merged_gdf.to_file("output.GeoJSON")
