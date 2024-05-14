import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nGroupby to find first order date for each group(salesman_id):')
result = df.groupby('salesman_id')['ord_date'].min()
print(result)