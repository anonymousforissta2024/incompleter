import pandas as pd
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'], 'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'], 'Age': [42, 52, 36, 21, 23], 'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}
df = pd.DataFrame(initial_data, columns=['First_name', 'Last_name', 'Age', 'City'])
df['Qualification'] = df['First_name'].map(new_data)
print(df)