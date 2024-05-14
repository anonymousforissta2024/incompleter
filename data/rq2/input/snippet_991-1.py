import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(orders_data)
result = orders_data.groupby('customer_id').agg({'purch_amt': ['mean', 'min', 'max']})
print('\nMean, min, and max values of purchase amount (purch_amt) group by customer id  (customer_id).')
print(result)