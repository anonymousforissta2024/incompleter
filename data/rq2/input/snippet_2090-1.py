import numpy as np
num_1d = np.arange(5)
print('One dimensional array:')
print(num_1d)
print('\nTwo dimensional array:')
print(num_2d)
for a, b in np.nditer([num_1d, num_2d]):
    print('%d:%d' % (a, b))