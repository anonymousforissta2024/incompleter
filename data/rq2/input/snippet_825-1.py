import numpy as np
print('Original arrays:')
print(arra1)
print('\nRecord array;')
result = np.core.records.fromarrays(arra1.T, names='col1, col2, col3', formats='S80, f8, i8')
print(result)