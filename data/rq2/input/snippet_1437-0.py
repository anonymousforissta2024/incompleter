import numpy as np
print('Original array:')
print(a)
print('Each element of the array is:')
for x in np.nditer(a):
    print(x, end=' ')