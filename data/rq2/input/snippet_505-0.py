import numpy as np
print('Original array:')
print(a)
q, r = np.linalg.qr(a)
print('qr factorization of the said array:')
print('q=\n', q, '\nr=\n', r)