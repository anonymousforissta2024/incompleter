#Source: https://stackoverflow.com/questions/41058857/python-list-comprehension-causes-nameerror-when-assigned-to-static-varible
from collections import namedtuple

class StateDatabase:
    State = namedtuple('State', ['name', 'capital'])
    db = [State(*args) for args in [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ]]