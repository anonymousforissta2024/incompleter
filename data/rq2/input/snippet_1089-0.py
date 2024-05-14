import numpy as np
print('Original flattened array:')
print(a)
print('Weighted average along the specified axis of the above flattened array:')
print(np.average(a, axis=1, weights=[1.0 / 4, 2.0 / 4, 2.0 / 4]))