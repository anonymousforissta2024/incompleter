import numpy as np
print('Given array:')
print(n_arr)
print('\nReplace all elements of array which are greater than 50. to 15.50')
n_arr[n_arr > 50.0] = 15.5
print('New array :\n')
print(n_arr)