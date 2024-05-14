import numpy as np
print('Original array:')
print(x)
print('Most frequent value in the above array:')
print(np.bincount(x).argmax())