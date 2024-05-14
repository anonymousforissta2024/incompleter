import numpy as np
np.set_printoptions(linewidth=100)
print('Original array:')
print(student)
char = 'E'
result = student[np.char.startswith(student[:, 2], char)]
print('\nStudent name starting with', char, ':')
print(result)
char = '1'
result = student[np.char.startswith(student[:, 0], char)]
print('\nStudent id starting with', char, ':')
print(result)