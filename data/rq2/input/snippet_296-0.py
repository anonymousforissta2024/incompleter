import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nInterpolate the missing values using the Linear Interpolation method (purch_amt):')
df['purch_amt'].interpolate(method='linear', direction='forward', inplace=True)
print(df)