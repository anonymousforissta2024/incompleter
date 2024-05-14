import pandas as pd
print('Original DataFrame:')
print(df)
print('\nConvert index of the said dataframe into a column:')
df.reset_index(level=0, inplace=True)
print(df)