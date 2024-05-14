import numpy as np
print('Original array;')
print(x)
r1 = np.sign(x)
r2 = np.copy(x)
r2[r2 > 0] = 1
r2[r2 < 0] = -1
assert np.array_equal(r1, r2)
print('Element-wise indication of the sign for all elements of the said array:')
print(r1)