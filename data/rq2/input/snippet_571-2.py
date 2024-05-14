import numpy as np
print('First array:')
print(x)
y = np.array([5 + 6j, 7 + 8j])
print('Second array:')
print(y)
z = np.vdot(x, y)
print('Product of above two arrays:')
print(z)