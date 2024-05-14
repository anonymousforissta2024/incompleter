#Source: https://stackoverflow.com/questions/55944944/attempting-to-inherit-variable-from-parent-class-nameerror-name-r-is-not-def
class Circle(Point):

    def __init__(self, r):
        self.r = r

class Cylinder(Circle):

    def __init__(self,h):
        Circle.__init__(self,r)
        self.h = h