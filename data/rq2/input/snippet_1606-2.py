import pandas as pd
index_ = [pd.Period('02-2018'), pd.Period('04-2018'), pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]
df.index = index_
print(df)