import pandas as pd
import re as re
print('Original DataFrame:')
print(df)

def search_words(text):
    result = re.findall('\\b[^\\d\\W]+\\b', text)
    return ' '.join(result)
df['only_words'] = df['address'].apply(lambda x: search_words(x))
print('\nOnly words:')
print(df)