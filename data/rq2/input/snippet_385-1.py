import numpy as np
print('Original array:')
print(x)
y = np.empty_like(x)
y[:] = x
print('\nCopy of the said array:')
print(y)