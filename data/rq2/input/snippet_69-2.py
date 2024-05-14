import numpy as np
x = np.array([-180.0, -90.0, 90.0, 180.0])
r2 = np.deg2rad(x)
assert np.array_equiv(r1, r2)
print(r1)