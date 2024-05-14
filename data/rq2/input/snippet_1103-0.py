import numpy as np
x = np.array([10, 10, 20, 30, 30], float)
print(x)
print('Put 0 and 40 in first and fifth position of the above array')
x.put([0, 4], y)
print('Array x, after putting two values:')
print(x)