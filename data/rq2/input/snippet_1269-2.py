import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print('Original DataFrame:')
print(df)
groups = df.groupby(['customer_id', pd.cut(df.sales_id, 3)])
result = groups.size().unstack()
print(result)