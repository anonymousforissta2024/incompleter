import numpy as np
a = np.array([97, 101, 105, 111, 117])
print('Original arrays')
print(a)
print(b)
print('Elements from the second array  corresponding to elements in the first array  that are greater than 100 and less than 110:')
print(b[(100 < a) & (a < 110)])