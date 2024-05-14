import numpy as np
print('Original matrix:')
print(m)
result = np.linalg.cond(m)
print('Condition number of the said matrix:')
print(result)