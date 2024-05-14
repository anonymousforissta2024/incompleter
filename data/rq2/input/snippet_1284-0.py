import numpy as np
print('Original array:')
print(x)
s = x.tostring()
print('Binary string array:')
print(s)
print('Array using fromstring():')
y = np.fromstring(s)
print(y)