#Source: https://stackoverflow.com/questions/60345611/dont-understand-cause-of-this-typeerror-exception
import json
import pygal
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RC
from pygal.maps.world import World
from country_codes import get_country_code
#load data into a list
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)