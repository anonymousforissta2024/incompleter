import numpy as np
x, y = np.atleast_2d(a[:, 0], a[:, 1])
d = np.sqrt((x - x.T) ** 2 + (y - y.T) ** 2)
print(d)