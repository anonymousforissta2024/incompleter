import pandas as pd
df = pd.DataFrame(data)
a = df.sort_values(by='Science', ascending=0)
print('Sorting rows by Science:\n \n', a)