import pandas as pd
print('Original DataFrame:')
print(df)
df.index.name = 'Index_name'
print('\nSaid DataFrame with a title or name of the index column:')
print(df)