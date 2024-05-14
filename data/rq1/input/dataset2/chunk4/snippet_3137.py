#Source: https://stackoverflow.com/questions/71139387/typeerror-get-user-takes-1-positional-argument-but-2-were-given-for-twitter-b
import tweepy

api_key='xxx'
api_key_secret='xxx'
access_token='xxx'
access_token_secret='xxx'

authenticator=tweepy.OAuthHandler(api_key,api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

user = api.get_user("ammfoundation")

tweets_user=api.user_timeline(user_id=user.id)

for tweet in tweets_user:
    if not tweet.favorited:
        api.create_favorite(tweet.id)