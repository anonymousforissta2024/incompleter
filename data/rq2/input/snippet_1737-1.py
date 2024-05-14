import numpy as np
print('Printing First matrix:')
print(x)
y = np.array([8 + 7j, 5 + 6j])
print('Printing Second matrix:')
print(y)
z = np.vdot(x, y)
print('Product of first and second matrices are:')
print(z)