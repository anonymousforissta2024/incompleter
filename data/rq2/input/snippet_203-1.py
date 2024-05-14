import numpy as np
print('Original array:')
print(a)
result = np.where(np.logical_and(a >= 7, a <= 20))
print('\nElements within range: index position')
print(result)