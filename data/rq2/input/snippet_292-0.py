import numpy as np
print('Original array and shape:')
print(a)
print(a.shape)
print('--------------------------------')
tidx = np.random.randint(0, 3, 4)
print('tidex: ', tidx)
print('Result:')
print(a[tidx, np.arange(len(tidx)), :])