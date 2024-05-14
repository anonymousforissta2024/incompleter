import pandas as pd
print('Original DataFrame:')
print(df)
print('\nWhether Alphabetic values present in company_code column?')
df['company_code_is_alpha'] = list(map(lambda x: x.isalpha(), df['company_code']))
print(df)