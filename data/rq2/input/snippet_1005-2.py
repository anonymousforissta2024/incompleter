import numpy as np
print('Original arrays:')
print(arra1)
n = 4
i = 1 + (arra1.shape[0] - 4)
j = 1 + (arra1.shape[1] - 4)
result = np.lib.stride_tricks.as_strided(arra1, shape=(i, j, n, n), strides=arra1.strides + arra1.strides)
print('\nContiguous 4x4 blocks:')
print(result)