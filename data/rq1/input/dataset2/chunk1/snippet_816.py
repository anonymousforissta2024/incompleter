#Source: https://stackoverflow.com/questions/53402504/cant-loop-the-distance-between-two-locations-typeerror-numpy-float64-object
coords_1 = (lat[0][3], lang[0][3])
coords_2 = (lat[0][5], lang[0][5])
print(geopy.distance.distance(coords_1, coords_2).km)