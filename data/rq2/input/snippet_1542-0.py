import pandas as pd
initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'], 'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'], 'Age': [42, 52, 36, 21, 23], 'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']}
new_data = {'Ram': 'B.Com', 'Mohan': 'IAS', 'Tina': 'LLB', 'Jeetu': 'B.Tech', 'Meera': 'MBBS'}
df['Qualification'] = df['First_name'].map(new_data)
print(df)