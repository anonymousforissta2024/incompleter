import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
df_agg = df.groupby(['customer_id', 'salesman_id']).agg({'purch_amt': sum})
result = df_agg['purch_amt'].groupby(level=0, group_keys=False)
print("\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
print(result.nlargest())