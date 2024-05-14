import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nReplacing NaNs with the value from the previous row (purch_amt):')
df['purch_amt'].fillna(method='pad', inplace=True)
print(df)
print('\nReplacing NaNs with the value from the next row (sale_amt):')
df['sale_amt'].fillna(method='bfill', inplace=True)
print(df)