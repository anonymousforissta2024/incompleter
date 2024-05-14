import pandas as pd
print(df, '\n')
print('Check PG values in Position column:\n')
df1 = df['Position'].str.contains('PG')
print(df1)