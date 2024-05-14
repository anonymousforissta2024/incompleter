import pandas as pd
import re as re
print('Original DataFrame:')
print(df)

def remove_tags(string):
    result = re.sub('<.*?>', '', string)
    return result
df['with_out_tags'] = df['address'].apply(lambda cw: remove_tags(cw))
print("\nSentences without tags':")
print(df)