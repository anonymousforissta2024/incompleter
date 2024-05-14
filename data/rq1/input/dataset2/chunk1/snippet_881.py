#Source: https://stackoverflow.com/questions/50845106/matplotlib-ylabel-typeerror-str-object-is-not-callable
from numpy import *
from matplotlib import *

a = [1, 2, 3, 4, 5]
b = [2, 3, 2, 3, 2]
pyplot.plot(a, b)
pylab.xlabel("Time")
pylab.ylabel("Speed")