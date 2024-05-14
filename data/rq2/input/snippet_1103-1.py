import numpy as np
print(x)
print('Put 0 and 40 in first and fifth position of the above array')
y = np.array([0, 40, 60], float)
x.put([0, 4], y)
print('Array x, after putting two values:')
print(x)