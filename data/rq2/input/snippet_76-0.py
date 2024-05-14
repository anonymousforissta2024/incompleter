import pandas as pd
print('Original DataFrame:')
print(df)
print('\nNumeric values present in company_code column:')
df['company_code_is_digit'] = list(map(lambda x: x.isdigit(), df['company_code']))
print(df)