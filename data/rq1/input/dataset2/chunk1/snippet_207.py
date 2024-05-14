#Source: https://stackoverflow.com/questions/55558011/intenum-returning-attributeerror-cant-set-attribute
from magnitude import Magnitude, MValue
from derivative import Derivative, DValue

class Quantity:
    def __init__(self, magnitude, derivative):
        self.magnitude = magnitude
        self.derivative = derivative