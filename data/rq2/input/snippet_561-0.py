import numpy as np
print('Original array of string values:')
print(str1)
print("\nReplace '-' with '=' character in the said array of string values:")
print(np.char.strip(np.char.replace(str1, '-', '==')))
print("\nReplace '-' with ' ' character in the said array of string values:")
print(np.char.strip(np.char.replace(str1, '-', ' ')))