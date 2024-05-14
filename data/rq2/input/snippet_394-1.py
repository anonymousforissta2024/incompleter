import numpy as np
print('Original vector:')
print(nums)
bin_nums = (nums.reshape(-1, 1) & 2 ** np.arange(8) != 0).astype(int)
print('\nBinary representation of the said vector:')
print(bin_nums[:, ::-1])