import numpy as np
print('Original array:')
print(x)
v = np.array([20, 30, 40])
print('Vector:')
print(v)
print(x / v[:, None])