import pandas as pd
import numpy as np
raw_Data = {'Voter_name': ['Geek1', 'Geek2', 'Geek3', 'Geek4', 'Geek5', 'Geek6', 'Geek7', 'Geek8'], 'Voter_age': [15, 23, 25, 9, 67, 54, 42, np.NaN]}
df = pd.DataFrame(raw_Data, columns=['Voter_name', 'Voter_age'])
for age in df['Voter_age']:
    if age >= 18:
        eligible.append('Yes')
    elif age < 18:
        eligible.append('No')
    else:
        eligible.append('Not Sure')
df['Voter'] = eligible
print(df)