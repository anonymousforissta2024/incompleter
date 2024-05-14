import pandas as pd
print('Original DataFrame with single index:')
print(df)
date_of_birth = ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997']
idx = 3
print("\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
df.insert(loc=idx, column='date_of_birth', value=date_of_birth)
print(df)