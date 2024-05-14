#Source: https://stackoverflow.com/questions/60345611/dont-understand-cause-of-this-typeerror-exception
from pygal.maps.world import COUNTRIES
def get_country_code(country_name):
    """Return the pygal 2-digit country code for given country."""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    #if the country wasnt found,return none.
    return None