#Source: https://stackoverflow.com/questions/55894445/using-dataclass-and-getting-attributeerror-int-object-has-no-attribute-x
from dataclasses import dataclass, field, InitVar

@dataclass
class XYPoint:
    last_serial_no = 0
    x: float
    y: float = 0
    skip: InitVar[int] = 1
    serial_no: int = field(init=False)

    def __post_init__(self, skip):
        self.serial_no = self.last_serial_no + self.skip
        self.__class__.last_serial_no = self.serial_no

    def __add__(self, other):
        new = XYPoint(self.x, self. y)
        new.x += other.x
        new.y += other.y