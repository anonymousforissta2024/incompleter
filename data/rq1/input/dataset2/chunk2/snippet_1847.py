#Source: https://stackoverflow.com/questions/49868472/gmap-draw-typeerror-must-be-real-number-not-str
import gmplot

gmap = gmplot.GoogleMapPlotter.from_geocode("Los Angeles",10)

gmap.heatmap(lat_lon['latitude'], lat_lon['longitude'])

gmap.draw('crime_map.html')