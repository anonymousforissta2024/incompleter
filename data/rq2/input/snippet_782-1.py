import numpy as np
x, y = (z[:, 0], z[:, 1])
r = np.sqrt(x ** 2 + y ** 2)
t = np.arctan2(y, x)
print(r)
print(t)