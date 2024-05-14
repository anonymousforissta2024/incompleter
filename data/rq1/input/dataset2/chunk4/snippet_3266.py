#Source: https://stackoverflow.com/questions/72383930/attributeerror-c-object-attribute-y-is-read-only-when-using-slots
class C(object):
    __slots__ = ('x',)
    def __init__(self, v):
        self.x = v
    y = 123

c = C(5)
c.y = 12