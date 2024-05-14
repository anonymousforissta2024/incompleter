#Source: https://stackoverflow.com/questions/48387878/attributeerror-dataframe-object-has-no-attribute-to-datetime
tweets_df = pd.read_csv('valid_tweets.csv')

tweets_df['Time'] = tweets_df.to_datetime(tweets_df['Time'])
tweets_df.set_index('Time', drop=False, inplace=True)