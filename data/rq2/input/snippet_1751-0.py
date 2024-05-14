import numpy as np
np.histogram(a, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
hist, bins = np.histogram(a, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print()
print(hist)
print(bins)
print()