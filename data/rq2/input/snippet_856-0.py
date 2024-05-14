import pandas as pd
print('Original DataFrame:')
print(df)
print('\nIf a specified column starts with a specified string?')
df['company_code_starts_with'] = list(map(lambda x: x.startswith('ze'), df['company_code']))
print(df)