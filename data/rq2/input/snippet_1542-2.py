import pandas as pd
df = pd.DataFrame(initial_data, columns=['First_name', 'Last_name', 'Age', 'City'])
new_data = {'Ram': 'B.Com', 'Mohan': 'IAS', 'Tina': 'LLB', 'Jeetu': 'B.Tech', 'Meera': 'MBBS'}
df['Qualification'] = df['First_name'].map(new_data)
print(df)