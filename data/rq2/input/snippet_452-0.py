import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def test_num_great(text):
    result = re.findall('95[5-9]|9[6-9]\\d|[1-9]\\d{3,}', text)
    return ' '.join(result)
df['num_great'] = df['address'].apply(lambda x: test_num_great(x))
print('\nNumber greater than 940:')
print(df)