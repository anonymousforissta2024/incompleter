import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nDrop the rows where at least one element is missing:')
result = df.dropna()
print(result)