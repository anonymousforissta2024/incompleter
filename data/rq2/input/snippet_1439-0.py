import numpy as np
test_array = np.array([4, 5, 6])
print('Original Numpy array:')
print(np_array)
print('Searched array:')
print(test_array)
print('Index of the searched array in the original array:')
print(np.where((np_array == test_array).all(1))[0])