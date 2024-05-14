#Source: https://stackoverflow.com/questions/73271581/module-api-has-no-attribute-error-in-python
import api
import tweepy

users = {}

keys = open("keystwitter.txt", 'r')

CONSUMER_KEY = keys.readline().strip()
CONSUMER_SECRET = keys.readline().strip()
ACCESS_TOKEN = keys.readline().strip()
ACCESS_TOKEN_SECRET = keys.readline().strip()

TwitterAuth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
TwitterAuth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweeter = tweepy.API(TwitterAuth)

StinkyChesse = ['mandzio', 'ewroon', 'klaudiacroft']


def initialize():
    file = open("users.txt", "r")
    for data in file:
        user_name = data.strip()
        print(user_name)
        user_id = api.get_user_id(user_name)
        follows = api.get_all_follows(user_id)
        users[user_name] = [user_id, follows]
    print("Bot Launched")