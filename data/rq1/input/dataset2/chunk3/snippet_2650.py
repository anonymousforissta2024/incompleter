#Source: https://stackoverflow.com/questions/64885946/how-to-solve-typeerror-string-indices-must-be-integers-while-removing-specific
import pandas as pd

df = pd.read_csv("Sample data.csv")
df1 = pd.DataFrame()

df1['Sentiment'] = df['Sentiment'].apply(lambda x: x if x['compound'] <= 0 else None)     # remove compound dictionary entry more than 1
df1.dropna(inplace=True)           #remove none lines
print(df1)