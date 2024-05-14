import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
df['ord_date'] = pd.to_datetime(df['ord_date'])
print('\nYear wise Month wise purchase amount:')
result = df.groupby([df['ord_date'].dt.year, df['ord_date'].dt.month]).agg({'purch_amt': sum})
print(result)