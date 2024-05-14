import numpy as np
x = np.random.randint(0, 2, 6)
print('First array:')
print(x)
print('Second array:')
print(y)
print('Test above two arrays are equal or not!')
array_equal = np.allclose(x, y)
print(array_equal)