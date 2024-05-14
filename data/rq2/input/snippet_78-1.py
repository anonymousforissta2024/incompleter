import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.DataFrame({'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013], 'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6], 'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'], 'customer_id': [3002, 3001, 3001, 3003, 3002, 3002, 3001, 3004, 3003, 3002, 3003, 3001], 'salesman_id': [5002, 5003, 5001, 5003, 5002, 5001, 5001, 5003, 5003, 5002, 5003, 5001]})
print('Original Orders DataFrame:')
print(df)
print("\nSplit the said data on 'salesman_id', 'customer_id' wise:")
result = df.groupby(['salesman_id', 'customer_id'])
for name, group in result:
    print('\nGroup:')
    print(name)
    print(group)
print('\nDroping last two records:')
result1 = df.drop(df.groupby(['salesman_id', 'customer_id']).tail(n).index, axis=0)
print(result1)