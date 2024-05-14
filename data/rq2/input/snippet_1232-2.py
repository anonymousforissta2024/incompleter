import numpy as np
print('Original array:')
print(x)
a = np.random.uniform(0, 100)
print('Value to compare:')
print(a)
index = np.abs(x - a).argmin()
print(x[index])