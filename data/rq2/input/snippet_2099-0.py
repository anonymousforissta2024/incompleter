import numpy as np
array_2 = np.array([4, 6])
print('Array-1')
print(array_1)
print('\nArray-2')
print(array_2)
comb_array = np.array(np.meshgrid(array_1, array_2)).T.reshape(-1, 2)
print('\nCombine array:')
print(comb_array)