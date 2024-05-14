import numpy as np
b = np.array(['a', 'e', 'i', 'o', 'u'])
print('Original arrays')
print(a)
print(b)
print('Elements from the second array  corresponding to elements in the first array  that are greater than 100 and less than 110:')
print(b[(100 < a) & (a < 110)])