import pandas as pd
Row_list = []
for i in range(df.shape[0]):
    Row_list.append(list(df.iloc[i, :]))
print(Row_list[:3])