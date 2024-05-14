import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.DataFrame({'book_name': ['Book1', 'Book2', 'Book3', 'Book4', 'Book1', 'Book2', 'Book3', 'Book5'], 'book_type': ['Math', 'Physics', 'Computer', 'Science', 'Math', 'Physics', 'Computer', 'English'], 'book_id': [1, 2, 3, 4, 1, 2, 3, 5]})
print('Original Orders DataFrame:')
print(df)
print('\nNew column with count from groupby:')
print(result)