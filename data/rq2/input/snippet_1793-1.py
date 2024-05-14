import numpy
print('Array1:\n', array1)
array2 = numpy.array([[5, 6], [7, 8]])
print('\nArray2:\n', array2)
kroneckerProduct = numpy.kron(array1, array2)
print('\nArray1 ⊗ Array2:')
print(kroneckerProduct)