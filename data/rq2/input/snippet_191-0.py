import pandas as pd
print('Original DataFrame:')
print(df)
print('\nLength of the string in a column:')
df['company_code_length'] = df['company_code'].apply(len)
print(df)