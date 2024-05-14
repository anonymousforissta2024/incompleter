import numpy as np
print('Original array:')
print(a)
print('Frobenius norm and the condition number:')
print(np.linalg.norm(a, 'fro'))
print(np.linalg.cond(a, 'fro'))