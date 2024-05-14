import pandas as pd
print('Original DataFrame:')
print(df)
print('\nTitle cases:')
df['company_code_title_cases'] = list(map(lambda x: x.title(), df['company_code']))
print(df)