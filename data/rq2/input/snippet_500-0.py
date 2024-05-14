import pandas as pd
print('Original DataFrame:')
print(df)
print('\nLength of sale_amount:')
df['sale_amount_length'] = df['sale_amount'].map(str).apply(len)
print(df)