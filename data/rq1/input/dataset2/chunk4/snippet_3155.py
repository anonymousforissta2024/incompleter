#Source: https://stackoverflow.com/questions/65948454/attributeerror-owm-object-has-no-attribute-weather-at-coords
from python.owm import OWM
owm = OWM('API KEY')
mgr = owm.weather_manager()
lat = 0
lon = 0
current_weather = owm.weather_at_coords(lat, lon).weather
print(current_weather)