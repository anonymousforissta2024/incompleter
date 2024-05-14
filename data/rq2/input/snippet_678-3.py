import numpy as np
a = np.array([1, 2, 5])
print('Original 1-d arrays:')
print(a)
print(b)
print
result = np.inner(a, b)
print('Inner product of the said vectors:')
x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print('Higher dimension arrays:')
print(x)
print(y)
result = np.inner(x, y)
print('Inner product of the said vectors:')
print(result)