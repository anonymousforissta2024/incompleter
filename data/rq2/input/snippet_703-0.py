import numpy as np
n = 4
i = 3
e = 10
print('Original array:')
print(array_nums1)
np.put(array_nums1, np.random.choice(range(n * n), i, replace=False), e)
print('\nPlace a specified element in specified time randomly:')
print(array_nums1)