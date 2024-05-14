import numpy as np
r1 = np.radians(x)
r2 = np.deg2rad(x)
assert np.array_equiv(r1, r2)
print(r1)