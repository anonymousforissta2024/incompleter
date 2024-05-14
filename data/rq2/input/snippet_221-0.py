import numpy as np
x = np.array([1, 3, 5, 7, 0])
print('Original array: ')
print(x)
r2 = np.insert(np.append(np.diff(x), 200), 0, [0, 0])
assert np.array_equiv(r1, r2)
print('Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
print(r2)