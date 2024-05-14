#Source: https://stackoverflow.com/questions/54514394/typeerror-normalize-argument-2-must-be-str-not-series-with-a-dataframe-of-st
# get date out of the index to column    
df_news = df_news.reset_index()
# optional
df_news['Date'] = pd.to_datetime(df_news['Date'])
# groupby and output group rows as list
df_news = df_news.groupby('Date')['name'].apply(list)
df_news.head()