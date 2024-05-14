import numpy as np
print('Original array elements:')
print(x)
for a in np.nditer(x, op_flags=['readwrite']):
    a[...] = 3 * a
print('New array elements:')
print(x)