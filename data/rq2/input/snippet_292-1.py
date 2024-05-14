import numpy as np
a = np.random.randint(0, 10, (3, 4, 8))
print('Original array and shape:')
print(a)
print(a.shape)
print('--------------------------------')
print('tidex: ', tidx)
print('Result:')
print(a[tidx, np.arange(len(tidx)), :])