import numpy as np
print('Original array:')
print(x)
print('Replace all elements of the said array with .5 which are greater than .5')
x[x > 0.5] = 0.5
print(x)