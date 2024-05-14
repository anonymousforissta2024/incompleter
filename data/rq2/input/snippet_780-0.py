import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def find_punctuations(text):
    result = re.findall('[!"\\$%&\\\'()*+,\\-.\\/:;=#@?\\[\\\\\\]^_`{|}~]*', text)
    string = ''.join(result)
    return list(string)
df['nonalpha'] = df['company_code'].apply(lambda x: find_punctuations(x))
print('\nExtracting punctuation:')
print(df)