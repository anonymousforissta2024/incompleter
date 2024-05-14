#Source: https://stackoverflow.com/questions/71321991/accessing-c-sharp-dll-through-python-3-8-using-python-net-typeerror
import clr

clr.AddReference(r"calcsDLL")
from myDLL import calcs

calcs.Pipe_Area(0.2)