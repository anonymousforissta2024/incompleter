#Source: https://stackoverflow.com/questions/53064690/attributeerror-map-object-has-no-attribute-marker
import folium
from folium.plugins import MarkerCluster

map1 = folium.Map(location=SF_COORDINATES, zoom_start=12)
marker_cluster = MarkerCluster().add_to(map1) 

for each in data[0:MAX_RECORDS].iterrows():
    map1.Marker(location = [each[1]['Y'],each[1]['X']], 
    clustered_marker = True).add_to(marker_cluster)

display(map1)