#Source: https://stackoverflow.com/questions/74035325/attributeerror-module-tweepy-has-no-attribute-oauthhandler-when-creating-tw
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print(api.verify_credentials().screen_name)