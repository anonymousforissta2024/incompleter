import pandas as pd
student_data1 = pd.DataFrame({'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'], 'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 'marks': [200, 210, 190, 222, 199]})
dicts = [{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 203}, {'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}]
print('Original DataFrames:')
print(student_data1)
print('\nDictionary:')
print(s6)
combined_data = student_data1.append(dicts, ignore_index=True, sort=False)
print('\nCombined Data:')
print(combined_data)