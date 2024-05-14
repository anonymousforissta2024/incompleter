import numpy as np
x = np.array([-np.pi, -np.pi / 2, np.pi / 2, np.pi])
r2 = np.rad2deg(x)
assert np.array_equiv(r1, r2)
print(r1)