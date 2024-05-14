#Source: https://stackoverflow.com/questions/52954676/pandas-scatter-plot-typeerror
import matplotlib.pyplot as plt
import geopandas

shapefile = geopandas.GeoDataFrame.from_file('file.shp')

fig, ax = plt.subplots(1)

base = shapefile.plot(ax=ax)

df.plot.scatter('Long', 'Lat',  c=df['colC'], s=df['colD'], alpha=0.7, ax=base, colormap='viridis')