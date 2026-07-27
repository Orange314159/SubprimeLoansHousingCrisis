import geopandas         as gpd 
import matplotlib.pyplot as plt
import sys 
## First we need to process the data from the csv so we will import then take the cols that we need


file_name = sys.argv[1]
col_num = int(sys.argv[2])
merged_gdf = gpd.read_file(f"{file_name}")

columns = merged_gdf.columns.tolist()
print(columns)
vmin_val = merged_gdf[columns[col_num]].quantile(0.01)
vmax_val = merged_gdf[columns[col_num]].quantile(0.99)



## set fig size and stuff
fig, ax = plt.subplots(1, 1, figsize=(20, 12))

## Plotting with explicit vmin and zmax parameters so it does not over saturate
merged_gdf.plot(
    column=columns[col_num], ## this is the thing we are plotting 
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
        "label": columns[col_num],
        "orientation": "horizontal", ## fits better
        "pad": 0.05,
        "shrink": 0.7,
        "extend": "both"  ## because we capped at 90% max there are higher values so it should be arrow
    }
)

## just a bunch of basic things on display stuff
ax.set_title(f"{columns[col_num]} by US Census Tract", fontsize=16, fontweight="bold")
ax.axis("off")


plt.tight_layout()
plt.show()

