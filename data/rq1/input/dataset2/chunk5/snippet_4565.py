#Source: https://stackoverflow.com/questions/49543553/name-error-when-calculating-the-average-error-between-two-data-sets
import numpy
from numpy import *
import scipy
import scipy.stats
import matplotlib. pyplot as plt
import matplotlib.patches as patches
from pylab import *
import scipy.integrate
from operator import itemgetter, attrgetter
import sys

def main(argv):
    t = open(sys.argv[1])
    first1 = t.readline()

    tt = open(argv[2])
    second2 = tt.readline()
    return [first1], [second2]

def analysis(first1, second2):

    first = np.array(first1, dtype = np.float64)
    second = np.array(second2, dtype = np.float64)

    #Average error
    avgerr = (first - second).mean()

    return [avgerr]

analysis(first1, second2)

if __name__ == '__main__':
    sys.exit(main(sys.argv))