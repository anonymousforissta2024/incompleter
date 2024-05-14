import numpy as np
print('First array:')
print(x)
y = np.random.randint(0, 2, 6)
print('Second array:')
print(y)
print('Test above two arrays are equal or not!')
array_equal = np.allclose(x, y)
print(array_equal)