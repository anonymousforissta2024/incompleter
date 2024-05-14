import numpy as np
v = 4
n = x.flat[np.abs(x - v).argmin()]
print(n)