import pandas as pd
pd.set_option('display.max_rows', None)
print('Original Orders DataFrame:')
print(df)
print('\nNew column with count from groupby:')
result = df.groupby(['book_name', 'book_type'])['book_type'].count().reset_index(name='count')
print(result)