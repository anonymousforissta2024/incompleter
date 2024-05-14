import pandas as pd
import numpy as np
x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Original series:')
print(x)
print(y)
print('\nEuclidean distance between two said series:')
print(np.linalg.norm(x - y))