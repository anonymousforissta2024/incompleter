import numpy as np
x = np.array([1.0, 2.0, 0.2, 0.3])
print('Original array: ')
print(x)
r1 = np.reciprocal(x)
assert np.array_equal(r1, r2)
print('Reciprocal for all elements of the said array:')
print(r1)