import numpy as np
q = [[1, 2], [3, 4]]
print('original matrix:')
print(p)
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print('cross product of the said two vectors(p, q):')
print(result1)
print('cross product of the said two vectors(q, p):')
print(result2)