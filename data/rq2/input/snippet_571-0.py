import numpy as np
x = np.array([1 + 2j, 3 + 4j])
print('First array:')
print(x)
print('Second array:')
print(y)
z = np.vdot(x, y)
print('Product of above two arrays:')
print(z)