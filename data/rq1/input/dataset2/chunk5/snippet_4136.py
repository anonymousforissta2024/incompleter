#Source: https://stackoverflow.com/questions/56079085/how-do-i-overcome-the-typeerror-cannot-convert-the-series-to-class-float-er
import pandas as pd
from math import radians, cos, sin, asin, sqrt
# convert decimal degrees to radians 
lon1 = df1['from_lon'].map(radians)
lat1 = df1['from_lat'].map(radians)
lon2 = df1['dest_lon'].map(radians)
lat2 = df1['dest_lat'].map(radians)
# haversine formula 
dlon = lon2 - lon1 
dlat = lat2 - lat1 
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * asin(sqrt(a))
results = 3959.0 * c