import pandas as pd
s6 = pd.Series(['S6', 'Scarlette Fisher', 205], index=['student_id', 'name', 'marks'])
dicts = [{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 203}, {'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}]
print('Original DataFrames:')
print(student_data1)
print('\nDictionary:')
print(s6)
combined_data = student_data1.append(dicts, ignore_index=True, sort=False)
print('\nCombined Data:')
print(combined_data)