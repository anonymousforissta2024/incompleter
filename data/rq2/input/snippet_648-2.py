import numpy as np
a1 = np.array([1, 2, 3, 4])
a2 = np.array(['Red', 'Green', 'White', 'Orange'])
result = np.core.records.fromarrays([a1, a2, a3], names='a,b,c')
print(result[0])
print(result[1])
print(result[2])