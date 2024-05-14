import numpy as np
print('Original array:')
print(x)
y = np.ascontiguousarray(x).view(np.dtype((np.void, x.dtype.itemsize * x.shape[1])))
_, idx = np.unique(y, return_index=True)
unique_result = x[idx]
print('Unique rows of the above array:')
print(unique_result)