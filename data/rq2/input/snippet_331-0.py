import pandas as pd
print('Original DataFrame:')
print(df)
print('\nIs lower (company_code)?')
df['company_code_ul_cases'] = list(map(lambda x: x.islower(), df['company_code']))
print(df)
print('\nIs Upper (company_code)?')
df['company_code_ul_cases'] = list(map(lambda x: x.isupper(), df['company_code']))
print(df)