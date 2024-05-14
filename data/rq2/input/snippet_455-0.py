import pandas as pd
print('Original DataFrame:')
print(df)
print('Count unique values:')
print(df.groupby('value')['id'].nunique())