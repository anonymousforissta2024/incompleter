import numpy as np
v = np.array([1, 1, 0])
print('Original vector:')
print(v)
print('Original matrix:')
print(m)
result = np.empty_like(m)
for i in range(4):
    result[i, :] = m[i, :] + v
print('\nAfter adding the vector v to each row of the matrix m:')
print(result)