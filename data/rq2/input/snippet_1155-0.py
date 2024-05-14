import pandas as pd
import numpy as np
import datetime
from datetime import datetime, date
print('Time-series with two index labels:')
time_series = pd.Series(np.random.randn(2), dates)
print(time_series)
print('\nType of the index:')
print(type(time_series.index))