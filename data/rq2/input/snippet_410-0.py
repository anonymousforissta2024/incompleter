import numpy as np
print('Original array:')
print(a)
U, s, V = np.linalg.svd(a, full_matrices=False)
q, r = np.linalg.qr(a)
print('Factor of a given array  by Singular Value Decomposition:')
print('U=\n', U, '\ns=\n', s, '\nV=\n', V)