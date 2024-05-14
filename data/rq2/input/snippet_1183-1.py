import pandas as pd
pd.set_option('display.max_rows', None)
print('Original DataFrame:')
print(student_data)
print('\nMean, min, and max value of age for each school with customized column names:')
grouped_single = student_data.groupby('school_code').agg(Age_Mean=('age', 'mean'), Age_Max=('age', max), Age_Min=('age', min))
print(grouped_single)