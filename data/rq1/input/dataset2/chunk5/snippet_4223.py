#Source: https://stackoverflow.com/questions/54445088/nameerror-class-is-not-defined
class Position:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: Position) -> Position:
        return Position(self.x + other.x, self.y + other.y)