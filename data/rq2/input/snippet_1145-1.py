import pandas as pd
import numpy as np
np.random.RandomState(100)
print('Original Series:')
print(num_series)
print('Top 2 Freq:', num_series.value_counts())
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
print(num_series)