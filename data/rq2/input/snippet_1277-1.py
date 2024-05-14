import numpy as np
print('Original array: ')
print(x)
print('\nexp(x)-1 for all elements of the said array:')
r1 = np.expm1(x)
r2 = np.exp(x) - 1.0
assert np.allclose(r1, r2)
print(r1)