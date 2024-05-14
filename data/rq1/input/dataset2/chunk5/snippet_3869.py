#Source: https://stackoverflow.com/questions/62862895/attributeerror-map-object-has-no-attribute-simple-marker-in-folium
import folium
import pandas as pd
 
SF_COORDINATES = (37.76, -122.45)
crimedata = pd.read_csv('SFPD_Incidents_2015.csv')
 
# for speed purposes
MAX_RECORDS = 1000
  
# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=12)
 
# add a marker for every record in the filtered data, use a clustered view
for each in crimedata[0:MAX_RECORDS].iterrows():
    map.simple_marker(
        location = [each[1]['Y'],each[1]['X']], 
        clustered_marker = True)
  
display(map)