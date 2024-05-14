#Source: https://stackoverflow.com/questions/48387878/attributeerror-dataframe-object-has-no-attribute-to-datetime
tweets_df['Time'] = pd.to_datetime(tweets_df['Time'])
for index, row in tweets_df.iterrows():
    row['Time'].tz_localize('UTC').tz_convert('US/Eastern')