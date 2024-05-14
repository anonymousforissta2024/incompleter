import pandas as pd
import re as re
pd.set_option('display.max_columns', 10)
print('Original DataFrame:')
print(df)

def find_email(text):
    email = re.findall('[\\w\\.-][email protected][\\w\\.-]+', str(text))
    return ','.join(email)
df['email'] = df['name_email'].apply(lambda x: find_email(x))
print('\\Extracting email from dataframe columns:')
print(df)