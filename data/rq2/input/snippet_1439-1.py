import numpy as np
np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print('Original Numpy array:')
print(np_array)
print('Searched array:')
print(test_array)
print('Index of the searched array in the original array:')
print(np.where((np_array == test_array).all(1))[0])