import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print("\nSplit the said data on 'salesman_id', 'customer_id' wise:")
result = df.groupby(['salesman_id', 'customer_id'])
for name, group in result:
    print('\nGroup:')
    print(name)
    print(group)
n = 2
print('\nDroping last two records:')
result1 = df.drop(df.groupby(['salesman_id', 'customer_id']).tail(n).index, axis=0)
print(result1)