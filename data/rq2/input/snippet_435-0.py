import numpy as np
print('Original array')
print(a)
print('Checking for complex number:')
print(np.iscomplex(a))
print('Checking for real number:')
print(np.isreal(a))
print('Checking for scalar type:')
print(np.isscalar(3.1))
print(np.isscalar([3.1]))