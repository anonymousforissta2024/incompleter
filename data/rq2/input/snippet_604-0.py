import pandas as pd
print('Original DataFrame:')
print(df)
print('\nSwapp cases in comapny_code:')
df['swapped_company_code'] = list(map(lambda x: x.swapcase(), df['company_code']))
print(df)