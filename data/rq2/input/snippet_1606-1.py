import pandas as pd
df = pd.DataFrame({'City': ['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'], 'Event': ['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'], 'Cost': [10000, 5000, 15000, 2000, 12000]})
df.index = index_
print(df)