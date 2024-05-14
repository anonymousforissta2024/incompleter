import pandas as pd
import re as re
print('Original DataFrame:')
print(df)

def pick_only_key_sentence(str1, word):
    result = re.findall('([^.]*' + word + '[^.]*)', str1)
    return result
df['filter_sentence'] = df['address'].apply(lambda x: pick_only_key_sentence(x, 'Avenue'))
print("\nText with the word 'Avenue':")
print(df)