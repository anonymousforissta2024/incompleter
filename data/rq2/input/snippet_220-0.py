import numpy as np
print('Original array:')
print(a)
unique_elements, counts_elements = np.unique(a, return_counts=True)
print('Frequency of unique values of the said array:')
print(np.asarray((unique_elements, counts_elements)))