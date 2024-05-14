import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nReplace NaNs with a single constant value:')
result = df['ord_no'].fillna(0, inplace=False)
print(result)