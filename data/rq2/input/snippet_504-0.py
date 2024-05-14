import numpy as np
print('Original Array:')
print(x)
xmax, xmin = (x.max(), x.min())
x = (x - xmin) / (xmax - xmin)
print('After normalization:')
print(x)