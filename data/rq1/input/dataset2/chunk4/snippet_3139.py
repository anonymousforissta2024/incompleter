#Source: https://stackoverflow.com/questions/65369185/how-to-ignore-nonetype-error-in-tweet-id-statuses-lookup
def lookup_tweets(tweet_IDs, api):
    full_tweets = []
    tweet_count = len(tweet_IDs)
    try:
        for i in range((tweet_count // 100) + 1):
            # Catch the last group if it is less than 100 tweets
            end_loc = min((i + 1) * 100, tweet_count)
            full_tweets.extend(
                api.statuses_lookup(tweet_IDs[i * 100:end_loc], tweet_mode='extended')
            )
        return full_tweets
    except:
        pass

results = lookup_tweets(good_tweet_ids_test, api)
temp = json.dumps([status._json for status in results]) #create JSON
newdf = pd.read_json(temp, orient='records')
newdf.to_json('tweepy_tweets.json')