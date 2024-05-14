import numpy as np
x = np.array([10, -10, 10, -10, -10, 10])
print('Original arrays:')
print(x)
print(y)
result = np.sum((x == 10) & (y > 0.5))
print('\nNumber of instances of a value occurring in one array on the condition of another array:')
print(result)