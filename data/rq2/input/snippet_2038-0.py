import numpy as np
print('Original 3d array:\n', arr)
diag_arr = np.diagonal(arr, axis1=1, axis2=2)
print('2d diagonal array:\n', diag_arr)