import numpy as np
arra = np.array([[1, 1, 0], [0, 0, 0], [0, 2, 3], [0, 0, 0], [0, -1, 1], [0, 0, 0]])
print('Original array:')
print(arra)
temp = {(0, 0, 0)}
for idx, row in enumerate(map(tuple, arra)):
    if row not in temp:
        result.append(idx)
print('\nNon-zero unique rows:')
print(arra[result])