import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def test_num_less(n):
    nums = []
    for i in n.split():
        result = re.findall('\\b(0*(?:[1-9][0-9]?|100))\\b', i)
        nums.append(result)
        all_num = [','.join(x) for x in nums if x != []]
    return ' '.join(all_num)
df['num_less'] = df['address'].apply(lambda x: test_num_less(x))
print('\nNumber less than 100:')
print(df)