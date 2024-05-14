import numpy as np
matrix1 = np.array([[1, 2], [0, 2]])
print('Original matrix:')
print(matrix1)
print(matrix2)
result = np.einsum('mk,kn', matrix1, matrix2)
print('Einstein’s summation convention of the two matrix:')
print(result)