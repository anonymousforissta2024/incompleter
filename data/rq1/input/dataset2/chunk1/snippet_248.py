#Source: https://stackoverflow.com/questions/48387878/attributeerror-dataframe-object-has-no-attribute-to-datetime
tweets_df['Time'] = pd.to_datetime(tweets_df['Time'])
tweets_df.set_index('Time', drop=False, inplace=True)
tweets_df.index = tweets_df.index.tz_localize('UTC').tz_convert('US/Eastern') 