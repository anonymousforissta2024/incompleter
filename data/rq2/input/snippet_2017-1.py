import pandas as pd
df = pd.DataFrame(data)
print(df.loc[1:3, ['Name', 'Qualification']])