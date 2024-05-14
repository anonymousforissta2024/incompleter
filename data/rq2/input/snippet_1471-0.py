import numpy as numpy
print('Original array:')
print(array)
argsort_array = array.argsort()
ranks_array = numpy.empty_like(argsort_array)
ranks_array[argsort_array] = numpy.arange(len(array))
print('\nRank of each item of the said array:')
print(ranks_array)