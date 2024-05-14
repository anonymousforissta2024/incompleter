import numpy as np
arra1 = np.random.randint(0, 5, (12, 12))
print('Original arrays:')
print(arra1)
n = 4
i = 1 + (arra1.shape[0] - 4)
j = 1 + (arra1.shape[1] - 4)
print('\nContiguous 4x4 blocks:')
print(result)