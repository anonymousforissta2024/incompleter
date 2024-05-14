import numpy as np
print('Original array of string values:')
print(str1)
print("\nCount 'Python' row wise in the above array of string values:")
print(np.char.count(str1, 'Python'))