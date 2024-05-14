import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Original DataFrame:')
print(df)
print('\nGroup by one column and remove those groups if all the values of a specific columns are not available:')
result = df[(~df['height'].isna()).groupby(df['school_code']).transform('any')]
print(result)