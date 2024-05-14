import numpy as np
z = np.random.random((10, 2))
x, y = (z[:, 0], z[:, 1])
t = np.arctan2(y, x)
print(r)
print(t)