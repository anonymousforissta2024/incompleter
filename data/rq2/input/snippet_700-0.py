import numpy as np
print('Original array:')
print(x)
print('0 on the border and 1 inside in the array')
x = np.pad(x, pad_width=1, mode='constant', constant_values=0)
print(x)