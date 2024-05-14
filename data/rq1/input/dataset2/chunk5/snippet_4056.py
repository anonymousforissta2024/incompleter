#Source: https://stackoverflow.com/questions/61088917/getting-an-attributeerror-module-pandas-has-no-attribute-plotting-when-tr
import folium
map = folium.Map(location=[80, -100])
map.save("Map1.html")