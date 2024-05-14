#Source: https://stackoverflow.com/questions/49566391/nameerror-for-importing-random-and-numpy-random-but-nothing-else
from numpy.random import uniform
sample = {item: uniform() for item in [1,2,3]}