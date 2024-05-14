#Source: https://stackoverflow.com/questions/57203454/why-does-python-raise-a-nameerror-for-conditional-list-comprehensions-inside-cla
from collections import namedtuple

class StateDatabase:
    State = namedtuple('State', ['name', 'capital'])
    db = [State(*args) for args in [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        # ...
    ]]