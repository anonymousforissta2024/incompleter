import numpy as np
arra1 = np.ones((25, 25))
print('Original arrays:')
print(arra1)
result = np.add.reduceat(np.add.reduceat(arra1, np.arange(0, arra1.shape[0], k), axis=0), np.arange(0, arra1.shape[1], k), axis=1)
print('\nBlock-sum (5x5) of the said array:')
print(result)