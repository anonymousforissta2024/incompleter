#Source: https://stackoverflow.com/questions/53402504/cant-loop-the-distance-between-two-locations-typeerror-numpy-float64-object
import pandas as pd
import numpy as np
from pandas import DataFrame

Data = pd.read_csv('/home/aziz/Desktop/langlat.csv')
data = pd.DataFrame(Data)
lat1 = data['Lattude'][2:]
lat = pd.DataFrame(np.array(lat1))
lang1 = data['Langitude'][2:]
lang = pd.DataFrame(np.array(lang1))

import geopy.distance


for i in range(len(lat)):
    for j in range(len(lat)):
        coords_1 = (all(lat[0][i]), all(lang[0][i]))
        coords_2 = (all(lat[0][j]), all(lang[0][j]))
        print(geopy.distance.distance(coords_1, coords_2).km)