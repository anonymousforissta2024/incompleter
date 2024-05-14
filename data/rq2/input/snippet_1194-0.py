import pandas as pd
print('Original DataFrame:')
print(df)
result = df.groupby(['id', 'type', 'book']).size().unstack(fill_value=0)
print('\nResult:')
print(result)