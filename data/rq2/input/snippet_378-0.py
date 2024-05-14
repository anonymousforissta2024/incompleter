import numpy as np
print('Original array:')
print(x)
print('Sum of all elements:')
print(np.sum(x))
print('Sum of each column:')
print(np.sum(x, axis=0))
print('Sum of each row:')
print(np.sum(x, axis=1))