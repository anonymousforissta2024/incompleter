import pandas as pd
print('Original DataFrame:')
print(df)
print('\nIs proper case or title case?')
df['company_code_is_title'] = list(map(lambda x: x.istitle(), df['company_code']))
print(df)