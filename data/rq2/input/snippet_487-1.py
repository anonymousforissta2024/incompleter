import numpy as np
print('Original arrays:')
print(array_nums1)
result = array_nums1[(array_nums1 > 6) & (array_nums1 % 3 == 0)]
print('\nItems greater than 6 and a multiple of 3 of the said array:')
print(result)