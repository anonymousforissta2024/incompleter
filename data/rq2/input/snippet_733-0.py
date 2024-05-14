import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def find_number(text):
    num = re.findall('[0-9]+', text)
    return ' '.join(num)
df['number'] = df['address'].apply(lambda x: find_number(x))
print('\\Extracting numbers from dataframe columns:')
print(df)