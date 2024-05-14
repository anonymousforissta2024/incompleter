import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def find_phone_number(text):
    ph_no = re.findall('\\b\\d{10}\\b', text)
    return ''.join(ph_no)
df['number'] = df['company_phone_no'].apply(lambda x: find_phone_number(x))
print('\\Extracting numbers from dataframe columns:')
print(df)