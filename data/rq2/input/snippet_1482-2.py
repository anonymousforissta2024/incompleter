import numpy as np
np.set_printoptions(linewidth=100)
print('Original array:')
print(student)
char = 'E'
result = student[np.char.startswith(student[:, 2], char)]
print('\nTotal weight, where student name starting with', char)
print(np.round(result[:, 3].astype(float).sum(), 2))
char = 'D'
result = student[np.char.startswith(student[:, 2], char)]
print('\nTotal weight, where student name starting with', char)
print(np.round(result[:, 3].astype(float).sum(), 2))