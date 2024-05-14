import pandas as pd
df = pd.DataFrame(data, columns=['Name', 'Age', 'Stream', 'Percentage'])
print('Given Dataframe :\n', df)
print('\nIterating over rows using index attribute :\n')
for ind in df.index:
    print(df['Name'][ind], df['Stream'][ind])