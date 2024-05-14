import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def test_and_cond(text):
    result = re.findall('(?=.*Ave.)(?=.*9910).*', text)
    return ' '.join(result)
df['check_two_words'] = df['address'].apply(lambda x: test_and_cond(x))
print('\nPresent two words!')
print(df)