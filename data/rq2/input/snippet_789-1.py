import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nMissing values in purch_amt column:')
result = df['purch_amt'].value_counts(dropna=False).loc[np.nan]
print(result)