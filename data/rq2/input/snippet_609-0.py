import numpy as np
x = np.arange(4)
print('One dimensional array:')
print(x)
print('Two dimensional array:')
print(y)
for a, b in np.nditer([x, y]):
    print('%d:%d' % (a, b))