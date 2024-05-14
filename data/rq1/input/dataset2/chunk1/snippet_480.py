#Source: https://stackoverflow.com/questions/64816277/why-do-i-get-a-nameerror-name-orientation-is-not-defined-in-python3
from collections import namedtuple

class StateDatabase:
    State = namedtuple('State', ['name', 'capital'])
    db = [State(*args) for args in [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ]]