import pandas as pd
df = pd.DataFrame(input_df)
print('Original DataFrame: \n', df)
print('\nRows iterated using iterrows() : ')
for index, row in df.iterrows():
    print(row['name'], row['age'])