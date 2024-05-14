import numpy as np
print('Original matrix:')
print(matrix)
result = np.linalg.cond(matrix)
print('Condition number of the matrix:')
print(result)