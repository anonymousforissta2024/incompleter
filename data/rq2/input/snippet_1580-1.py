import pandas as pd
import numpy as np
df = pd.DataFrame(raw_Data, columns=['Voter_name', 'Voter_age'])
eligible = []
for age in df['Voter_age']:
    if age >= 18:
        eligible.append('Yes')
    elif age < 18:
        eligible.append('No')
    else:
        eligible.append('Not Sure')
df['Voter'] = eligible
print(df)