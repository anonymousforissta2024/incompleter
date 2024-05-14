import numpy as np
print('Original array elements:')
print(x)
print('Above array in small chuncks:')
for a in np.nditer(x, flags=['external_loop'], order='F'):
    print(a)