import pandas as pd
pd.set_option('display.max_rows', None)
print('Original DataFrame:')
print(df)
print('\nGroup by with multiple aggregations:')
result = df.groupby(['school_code', 'class']).agg({'height': ['max', 'mean'], 'weight': ['sum', 'min', 'count']})
print(result)