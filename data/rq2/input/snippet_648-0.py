import numpy as np
a1 = np.array([1, 2, 3, 4])
a3 = np.array([12.2, 15, 20, 40])
result = np.core.records.fromarrays([a1, a2, a3], names='a,b,c')
print(result[0])
print(result[1])
print(result[2])