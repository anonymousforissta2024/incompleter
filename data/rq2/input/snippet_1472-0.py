import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(orders_data)
print('\nGroup by two columns and count by each row:')
result = orders_data.groupby(['salesman_id', 'customer_id']).size().reset_index().groupby(['salesman_id', 'customer_id'])[[0]].max()
print(result)