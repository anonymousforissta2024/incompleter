import pandas as pd
import re as re
print('Original DataFrame:')
print(df)

def find_unique_sentence(str1):
    result = re.findall('(?sm)(^[^\\r\\n]+$)(?!.*^\\1$)', str1)
    return result
df['unique_sentence'] = df['address'].apply(lambda st: find_unique_sentence(st))
print('\nExtract unique sentences :')
print(df)