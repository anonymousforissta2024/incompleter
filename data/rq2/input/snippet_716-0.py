import pandas as pd
print('Original DataFrame:')
print(df)
print('\nDefault Index Range:')
print(df.index)
df.index += 10
print('\nNew Index Range:')
print(df.index)
print('\nDataFrame with new index:')
print(df)