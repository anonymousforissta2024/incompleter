import pandas as pd
import re as re
print('Original DataFrame:')
print(df)

def find_valid_dates(dt):
    result = re.findall('\\b(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})\\b', dt)
    return result
df['valid_dates'] = df['date_of_sale'].apply(lambda dt: find_valid_dates(dt))
print('\nValid dates (format: mm-dd-yyyy):')
print(df)