#Source: https://stackoverflow.com/questions/73698056/i-am-new-to-pandas-data-frame-i-am-getting-this-error-typeerror-can-only-conca
import pandas as pd
import numpy as np
df = pd.read_excel("test123.xlsx")
print(df)
subone = df["F1"] + df["I1"]
print(subone)