#Source: https://stackoverflow.com/questions/53936383/folium-geo-mapping-leads-to-typeerror-must-be-real-number-not-str-while
#!/usr/bin/env python
import pandas as pd
import requests
from xml.etree import ElementTree
import numpy as np
import folium

xml_data = "coords.xml"

tree = ElementTree.parse(xml_data)
counter = tree.find('counter')

id = []
name = []
latitude = []
longitude = []

for c in tree.findall('counter'):
    id.append(c.attrib['id'])
    name.append(c.find('name').text)
    latitude.append(c.find('latitude').text)
    longitude.append(c.find('longitude').text)

df_counters = pd.DataFrame(
    {'ID' : id,
    'Name' : name,
    'latitude' : latitude,
    'longitude' : longitude
    })
df_counters.head()

locations = df_counters[['latitude', 'longitude']]
locationlist = locations.values.tolist()

map = folium.Map(location=[47.3, 5.2], zoom_start=10)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=df_counters['Name'][point]).add_to(map)
map