import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nKeep the said DataFrame with valid entries:')
result = df.dropna(inplace=False)
print(result)