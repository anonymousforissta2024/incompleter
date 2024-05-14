import numpy as np
import os
print('Original array:')
print(x)
header = 'col1 col2 col3'
np.savetxt('temp.txt', x, fmt='%d', header=header)
print('After loading, content of the text file:')
result = np.loadtxt('temp.txt')
print(result)