import pandas as pd
print('Original DataFrame with single index:')
print(df)
print('\nIndex of rows where specified column matches certain value:')
print(df.index[df['school_code'] == 's001'].tolist())