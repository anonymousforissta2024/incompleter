import numpy as np
print('Original array: ')
print(x)
r1 = np.around(x)
r2 = np.floor(x)
r3 = np.ceil(x)
r4 = np.trunc(x)
r5 = [round(elem) for elem in x]
print('\naround:   ', r1)
print('floor:    ', r2)
print('ceil:     ', r3)
print('trunc:    ', r4)
print('round:    ', r5)