import numpy as np
print('Original array: ')
print(x)
print('Values bigger than 10 =', x[x > 10])
print('Their indices are ', np.nonzero(x > 10))