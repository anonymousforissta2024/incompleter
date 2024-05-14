import numpy as np
print('Original array:')
print(a)
i, j = np.unravel_index(a.argmax(), a.shape)
print('Index of a maximum element in a numpy array along one axis:')
print(a[i, j])