#Source: https://stackoverflow.com/questions/49425270/attribute-error-map-object-has-no-attribute-create-map
import folium
map_osm = folium.Map(location=[45.5236, -122.6750])
map_osm.create_map(path='osm.html')