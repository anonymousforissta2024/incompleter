import numpy as np
import os
x = np.arange(12).reshape(4, 3)
print('Original array:')
print(x)
np.savetxt('temp.txt', x, fmt='%d', header=header)
print('After loading, content of the text file:')
result = np.loadtxt('temp.txt')
print(result)