import numpy as np
matrix2 = np.array([[0, 1], [3, 4]])
print('Original matrix:')
print(matrix1)
print(matrix2)
result = np.einsum('mk,kn', matrix1, matrix2)
print('Einstein’s summation convention of the two matrix:')
print(result)