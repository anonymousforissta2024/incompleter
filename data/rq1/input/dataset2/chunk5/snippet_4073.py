#Source: https://stackoverflow.com/questions/51049124/importing-from-file-vs-internet-in-genfromtxt-numpy-date-typeerror-must-be-str
import numpy as np
from matplotlib.dates import bytespdate2num

names = ["A", "B", "C", "D", "E", "F", "G"]
my_array1 = np.genfromtxt("goog.csv",                     
                          delimiter=',',
                          skip_header=1,
                          names=names,
                          dtype=None,
                          converters={0: bytespdate2num('%Y-%m-%d')})
print(my_array1["A"])