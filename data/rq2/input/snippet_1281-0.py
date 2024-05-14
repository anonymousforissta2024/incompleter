import numpy as np
array1 = ['PHP', 'JS', 'C++']
print('Original arrays:')
print(array1)
print(array2)
result = np.r_[array1[:-1], [array1[-1] + array2[0]], array2[1:]]
print('\nAfter Combining:')
print(result)