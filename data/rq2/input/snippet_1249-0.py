import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def find_nonalpha(text):
    result = re.findall('[^A-Za-z0-9 ]', text)
    return result
df['nonalpha'] = df['company_code'].apply(lambda x: find_nonalpha(x))
print('\\Extracting only non alphanumeric characters from company_code:')
print(df)