import numpy as np
r1 = np.degrees(x)
r2 = np.rad2deg(x)
assert np.array_equiv(r1, r2)
print(r1)