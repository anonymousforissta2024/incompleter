import numpy as np
print('Original matrix:')
print(m)
result = np.linalg.qr(m)
print('Decomposition of the said matrix:')
print(result)