import numpy as np
print('Given array:', arr)
sorted_index_array = np.argsort(arr)
sorted_array = arr[sorted_index_array]
print('Sorted array:', sorted_array)
n = 1
rslt = sorted_array[-n:]
print('{} largest value:'.format(n), rslt[0])