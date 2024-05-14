import pandas as pd
pd.set_option('display.max_rows', None)
print('Original DataFrame:')
print(df)
print('\nSplit the data on school_code:')
gp = df.groupby('school_code')
print('\nList of all the keys:')
print(gp.groups.keys())