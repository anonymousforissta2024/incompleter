import numpy as np
print('Original matrix:')
print('a\n', m)
w, v = np.linalg.eig(m)
print('Eigenvalues of the said matrix', w)
print('Eigenvectors of the said matrix', v)