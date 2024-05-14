#Source: https://stackoverflow.com/questions/58275685/attributeerror-type-object-pandana-cyaccess-cyaccess-has-no-attribute-redu
import pandana, time, os, pandas as pd, numpy as np
from pandana.loaders import osm

# define your selected amenities and bounding box
# configure search at a max distance of 1 km for up to the 10 nearest points-of-interest
amenities = ['restaurant', 'bar', 'food']
distance = 1000
num_pois = 10
num_categories = len(amenities) + 1 #one for each amenity, plus one extra for all of them combined

# bounding box as a list of llcrnrlat, llcrnrlng, urcrnrlat, urcrnrlng
# Bounding box for a Edinburgh, Scotland
west, south, east, north = (-3.449533, 55.818792, -3.074951, 56.004084)
bbox = [west, south, east, north] #lat-long bounding box for Edinburgh, Scotland