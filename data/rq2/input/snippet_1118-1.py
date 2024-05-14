import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nKeep the rows with at least 2 NaN values of the said DataFrame:')
result = df.dropna(thresh=2)
print(result)