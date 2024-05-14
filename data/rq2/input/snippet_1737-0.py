import numpy as np
x = np.array([2 + 3j, 4 + 5j])
print('Printing First matrix:')
print(x)
print('Printing Second matrix:')
print(y)
z = np.vdot(x, y)
print('Product of first and second matrices are:')
print(z)