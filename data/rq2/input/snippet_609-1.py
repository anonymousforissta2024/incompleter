import numpy as np
print('One dimensional array:')
print(x)
y = np.arange(8).reshape(2, 4)
print('Two dimensional array:')
print(y)
for a, b in np.nditer([x, y]):
    print('%d:%d' % (a, b))