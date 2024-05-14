import pandas as pd
print('Original DataFrame:')
print(df)
print('\nIs space is present?')
df['company_code_is_title'] = list(map(lambda x: x.isspace(), df['company_code']))
print(df)