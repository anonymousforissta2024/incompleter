import pandas as pd
pd.set_option('display.max_rows', None)
print('Original DataFrame:')
print(student_data)
print('\nCast grouping as a list:')
result = student_data.groupby(['school_code'])
print(list(result))