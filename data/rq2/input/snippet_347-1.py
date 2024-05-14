import pandas as pd
s1 = pd.Series([0, 1, 2, 3], name='col1')
s2 = pd.Series([0, 1, 2, 3])
df = pd.concat([s1, s2, s3], axis=1, keys=['column1', 'column2', 'column3'])
print(df)