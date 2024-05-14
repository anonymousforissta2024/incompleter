import numpy as np
print('Original array:')
print(arra)
temp = {(0, 0, 0)}
result = []
for idx, row in enumerate(map(tuple, arra)):
    if row not in temp:
        result.append(idx)
print('\nNon-zero unique rows:')
print(arra[result])