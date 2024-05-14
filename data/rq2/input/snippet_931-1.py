import numpy as np
x = np.array([[20, 20, 20, 0], [0, 20, 20, 20], [0, 20, 20, 20], [20, 20, 20, 0], [10, 20, 20, 20]])
print('Original array:')
print(x)
_, idx = np.unique(y, return_index=True)
unique_result = x[idx]
print('Unique rows of the above array:')
print(unique_result)