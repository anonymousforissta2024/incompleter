import numpy as np
print('Original array: ')
print(a)
print('Sort along the first axis: ')
x = np.sort(a, axis=0)
print(x)
print('Sort along the last axis: ')
y = np.sort(x, axis=1)
print(y)