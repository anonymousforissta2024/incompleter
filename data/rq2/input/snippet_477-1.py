import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nReplace the missing values with NaN:')
result = df.replace({'?': np.nan, '--': np.nan})
print(result)