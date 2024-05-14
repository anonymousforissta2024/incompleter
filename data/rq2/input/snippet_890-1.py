import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nDrop those rows in which specific columns have missing values:')
result = df.dropna(subset=['ord_no', 'customer_id'])
print(result)