import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nReplace the missing values with the most frequent values present in each column:')
result = df.fillna(df.mode().iloc[0])
print(result)