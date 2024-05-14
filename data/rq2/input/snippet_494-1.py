import numpy as np
print('Original array:')
print(a)
L = np.linalg.cholesky(a)
print('Lower-trianglular L in the Cholesky decomposition of the said array:')
print(L)