#Source: https://stackoverflow.com/questions/75650571/nameerror-name-df-is-not-definedpython
import pandas as pd
# Using DataFrame.astype() function
df["Date"] = df["Date"].astype('datetime64[ns]')
print (df.dtypes)