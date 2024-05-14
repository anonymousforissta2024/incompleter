import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
result = df.groupby('customer_id')['ord_date'].apply(list)
print("\nGroup on 'customer_id' and display the list of order dates in group wise:")
print(result)