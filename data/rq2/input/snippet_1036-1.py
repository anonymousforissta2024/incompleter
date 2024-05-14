import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nDrop the rows where all elements are missing:')
result = df.dropna(how='all')
print(result)