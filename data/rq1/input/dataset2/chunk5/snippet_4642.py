#Source: https://stackoverflow.com/questions/66753663/attributeerror-object-has-no-attribute-python-error
class PointType(Point):

    def __init__(self, i: int, j: int, t: int):
        Point.__init__(self, i, j)
        self.__t = t

    # getters and setters