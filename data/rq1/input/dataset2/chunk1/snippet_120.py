#Source: https://stackoverflow.com/questions/48387878/attributeerror-dataframe-object-has-no-attribute-to-datetime
for index, row in tweets_df.iterrows():
    print(row['Time'])