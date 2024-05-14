#Source: https://stackoverflow.com/questions/57698072/typeerror-list-indices-must-be-integers-or-slices-not-str-in-regression-anal
import pandas as pd
import quandl
df= quandl.get("FINRA/FORF_SYNVP", authtoken="sF7es4t9ozY6QjvZyL9M")
df=[['ShortVolume','TotalVolume']]
df['change_PCT']=(df['TotalVolume']-df['ShortVolume'])/df['ShortVolume']*100
df=df[['change_PCT','ShortVolume']]
print(df.head())