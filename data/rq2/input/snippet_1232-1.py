import numpy as np
x = np.arange(100)
print('Original array:')
print(x)
print('Value to compare:')
print(a)
index = np.abs(x - a).argmin()
print(x[index])