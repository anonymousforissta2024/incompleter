#Source: https://stackoverflow.com/questions/25178925/i-dont-understand-this-typeerror
class vector2D:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    @classmethod
    def frompoints(cls, P1, P2):
        x = P2[0] - P1[0]
        y = P2[1] - P1[1]
        return vector2D(cls, x, y)

P1 = (10.0, 5.0)
P2 = (17.0, 10.0)
v2 = vector2D.frompoints(P1, P2)