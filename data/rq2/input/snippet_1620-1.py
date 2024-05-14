import numpy
arr = numpy.array([[1, 2, 3, 4, 5], [10, -3, 30, 4, 5], [3, 2, 5, -4, 5], [9, 7, 3, 6, 5]])
print('Given Array:\n', arr)
output = numpy.where(numpy.any(arr > X, axis=1))
print('Result:\n', output)