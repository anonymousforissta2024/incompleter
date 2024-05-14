import numpy as numpy
array = numpy.array([24, 27, 30, 29, 18, 14])
print('Original array:')
print(array)
argsort_array = array.argsort()
ranks_array[argsort_array] = numpy.arange(len(array))
print('\nRank of each item of the said array:')
print(ranks_array)