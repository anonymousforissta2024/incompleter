import numpy as np
y = np.array([0.85, 0.45, 0.9, 0.8, 0.12, 0.6])
print('Original arrays:')
print(x)
print(y)
result = np.sum((x == 10) & (y > 0.5))
print('\nNumber of instances of a value occurring in one array on the condition of another array:')
print(result)