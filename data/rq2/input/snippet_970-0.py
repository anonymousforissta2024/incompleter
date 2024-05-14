import numpy as np
print('Original array:')
print(x)
x[x.argmax()] = -1
print('Maximum value replaced by -1:')
print(x)