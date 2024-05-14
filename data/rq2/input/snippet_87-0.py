import pandas as pd
print('Original dataframe:')
df = pd.DataFrame(nums)
print(df)
print('\nAdd leading zeros:')
df['amount'] = list(map(lambda x: x.zfill(10), df['amount']))
print(df)