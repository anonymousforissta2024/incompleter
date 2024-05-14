import pandas as pd
print('Original DataFrame:')
print(df)
result = df.groupby('X').aggregate(lambda tdf: tdf.unique().tolist())
print(result)