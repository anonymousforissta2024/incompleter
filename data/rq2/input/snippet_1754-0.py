import pandas as pd
input_df = [{'name': 'Sujeet', 'age': 10}, {'name': 'Sameer', 'age': 11}, {'name': 'Sumit', 'age': 12}]
print('Original DataFrame: \n', df)
print('\nRows iterated using iterrows() : ')
for index, row in df.iterrows():
    print(row['name'], row['age'])