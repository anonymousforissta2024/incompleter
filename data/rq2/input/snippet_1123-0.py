import numpy as np
x = np.array([1, 3, 5, 0, -1, -7, 0, 5])
print('Original array;')
print(x)
r2 = np.copy(x)
r2[r2 > 0] = 1
r2[r2 < 0] = -1
assert np.array_equal(r1, r2)
print('Element-wise indication of the sign for all elements of the said array:')
print(r1)