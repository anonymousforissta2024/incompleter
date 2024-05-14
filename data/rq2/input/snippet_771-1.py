import pandas as pd
import numpy as np
num_state = np.random.RandomState(100)
num_series = pd.Series(num_state.normal(10, 4, 20))
print('Original Series:')
print(num_series)
print('\nMinimum, 25th percentile, median, 75th, and maximum of a given series:')
print(result)