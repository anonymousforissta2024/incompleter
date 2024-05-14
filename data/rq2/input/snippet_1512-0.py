import pandas as pd
data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'], 'Age': [21, 19, 20, 18], 'Stream': ['Math', 'Commerce', 'Arts', 'Biology'], 'Percentage': [88, 92, 95, 70]}
print('Given Dataframe :\n', df)
print('\nIterating over rows using index attribute :\n')
for ind in df.index:
    print(df['Name'][ind], df['Stream'][ind])