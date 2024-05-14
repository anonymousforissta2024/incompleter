import numpy as np
x = np.array([0, 1, -1])
print('Original array: ')
print(x)
r1 = np.negative(x)
assert np.array_equal(r1, r2)
print('Numerical negative value for all elements of the said array:')
print(r1)