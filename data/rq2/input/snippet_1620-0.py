import numpy
X = 6
print('Given Array:\n', arr)
output = numpy.where(numpy.any(arr > X, axis=1))
print('Result:\n', output)