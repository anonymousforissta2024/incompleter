import numpy as np
print('Original array:')
print(x)
print('Remove all non-numeric elements of the said array')
print(x[~np.isnan(x).any(axis=1)])