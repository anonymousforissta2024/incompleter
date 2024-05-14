import pandas as pd
import numpy as np
print('Original series:')
print(nums)
print('\nPositions of the values surrounded by smaller values on both sides:')
temp = np.diff(np.sign(np.diff(nums)))
result = np.where(temp == -2)[0] + 1
print(result)