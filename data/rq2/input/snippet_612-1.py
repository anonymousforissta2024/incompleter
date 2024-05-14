import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nMissing values in purch_amt column:')
result = df['ord_no'].isnull().to_numpy().nonzero()
print(result)