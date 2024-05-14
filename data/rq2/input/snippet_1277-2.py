import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0], np.float32)
print('Original array: ')
print(x)
print('\nexp(x)-1 for all elements of the said array:')
r2 = np.exp(x) - 1.0
assert np.allclose(r1, r2)
print(r1)