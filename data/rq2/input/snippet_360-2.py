import numpy as np
import os
print('Original array:')
print(a)
a_bytes = a.tostring()
a2 = np.fromstring(a_bytes, dtype=a.dtype)
print('After loading, content of the text file:')
print(a2)
print(np.array_equal(a, a2))