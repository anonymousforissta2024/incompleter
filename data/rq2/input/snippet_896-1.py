import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
df['ord_date'] = pd.to_datetime(df['ord_date'])
print('\nQuartly purchase amount:')
result = df.set_index('ord_date').groupby(pd.Grouper(freq='Q')).agg({'purch_amt': sum})
print(result)