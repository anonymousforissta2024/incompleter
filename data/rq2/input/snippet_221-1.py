import numpy as np
print('Original array: ')
print(x)
r1 = np.ediff1d(x, to_begin=[0, 0], to_end=[200])
r2 = np.insert(np.append(np.diff(x), 200), 0, [0, 0])
assert np.array_equiv(r1, r2)
print('Difference between neighboring elements, element-wise, and prepend [0, 0] and append[200] to the said array:')
print(r2)