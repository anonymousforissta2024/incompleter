import numpy as np
import os
a = np.array([1, 2, 3, 4, 5, 6])
print('Original array:')
print(a)
a_bytes = a.tostring()
print('After loading, content of the text file:')
print(a2)
print(np.array_equal(a, a2))