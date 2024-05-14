import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('Using median in purch_amt to replace NaN:')
df['purch_amt'].fillna(df['purch_amt'].median(), inplace=True)
print(df)
print('Using mean to replace NaN:')
df['sale_amt'].fillna(int(df['sale_amt'].mean()), inplace=True)
print(df)