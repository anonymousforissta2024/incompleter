import numpy as np
print('Original array: ')
print(x)
r1 = np.reciprocal(x)
r2 = 1 / x
assert np.array_equal(r1, r2)
print('Reciprocal for all elements of the said array:')
print(r1)