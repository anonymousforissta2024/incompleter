#Source: https://stackoverflow.com/questions/54318925/basemap-typeerror-input-must-be-an-array-list-tuple-or-scalar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

data = pd.ExcelFile('C:\\Users\\...xlsx')
data_input = pd.read_excel(data, 'Sheet2')

# Extract the data we're interested in
lat = data_input['value1'].values
lon = data_input['value2'].values
capacity = data_input['value3'].values

# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=31.1351682, lon_0=-99.3350553,
            width=1.3E6, height=1.25E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# 2. scatter city data, with color reflecting population
# and size reflecting area
m.scatter(lon, lat, latlon=True,
          c=np.log10(capacity), s=capacity,
          cmap='Reds', alpha=0.5)