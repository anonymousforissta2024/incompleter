import numpy as np
print('Elements of the array in Fortan array:')
for x in np.nditer(x, order='F'):
    print(x, end=' ')
print('\n')