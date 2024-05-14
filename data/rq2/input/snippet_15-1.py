import pandas as pd
df = pd.DataFrame({'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'], 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 'weight': [35, 32, 33, 30, 31, 32]}, index=[1, 2, 3, 4, 5, 6])
print('Original DataFrame with single index:')
print(df)
date_of_birth = ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997']
print("\nInsert 'date_of_birth' column in 3rd position of the said DataFrame:")
df.insert(loc=idx, column='date_of_birth', value=date_of_birth)
print(df)