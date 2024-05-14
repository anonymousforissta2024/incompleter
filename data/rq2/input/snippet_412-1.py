import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nTotal number of missing values of the said DataFrame:')
result = df.isna().sum().sum()
print(result)