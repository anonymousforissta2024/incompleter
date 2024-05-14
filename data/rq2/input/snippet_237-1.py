import numpy as np
print('Original array: ')
print(x)
r1 = np.negative(x)
r2 = -x
assert np.array_equal(r1, r2)
print('Numerical negative value for all elements of the said array:')
print(r1)