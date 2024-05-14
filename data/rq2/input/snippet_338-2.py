import numpy as np
x = np.random.uniform(1, 12, 5)
n = x.flat[np.abs(x - v).argmin()]
print(n)