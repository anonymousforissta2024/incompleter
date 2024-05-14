import numpy
array1 = numpy.array([[1, 2], [3, 4]])
print('Array1:\n', array1)
print('\nArray2:\n', array2)
kroneckerProduct = numpy.kron(array1, array2)
print('\nArray1 ⊗ Array2:')
print(kroneckerProduct)