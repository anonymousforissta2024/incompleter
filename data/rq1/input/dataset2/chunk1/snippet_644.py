#Source: https://stackoverflow.com/questions/54263271/attributeerror-unknown-property-column-in-geopandas-plotting-of-events-in-zipco
# set a variable that will call column to visualise on the map

variable = 'ZIPNUM'

# set the range for the choropleth

vmin, vmax = 50, 2000

# create figure and axes for Matplotlib

fig, ax = plt.subplots(1, figsize=(15, 15))

# create map

merged_df.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8');

ax.axis('off')

ax.set_title('Fire Incident Rate in Wake County', fontdict={'fontsize': '25', 'fontweight' : '3'})

# Create colorbar as a legend

sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))

# empty array for the data range

sm._A = []

# add the colorbar to the figure

cbar = fig.colorbar(sm)

ax.annotate('2008-2018',
            xy=(0.001, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=35)

fig.savefig("Fire Incident Rate in Wake County 2008-2018.png", dpi=300)