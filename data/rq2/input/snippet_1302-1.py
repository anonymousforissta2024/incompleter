import pandas as pd
pd.set_option('display.max_rows', None)
print('Original DataFrame:')
print(df)
print('\nChange the name of an aggregated metric:')
grouped_single = df.groupby('school_code').agg({'age': [('mean_age', 'mean'), ('min_age', 'min'), ('max_age', 'max')]})
print(grouped_single)