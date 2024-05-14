#Source: https://stackoverflow.com/questions/55107435/how-to-load-statuses-from-twitter-api-typeerror-string-indices-must-be-integer
import oauth2 as oauth
import json
import configparser

config = configparser.RawConfigParser()
configpath = r'config.py'
config.read(configpath)
consumer_key = config.get('logintwitter', 'consumer_key')
consumer_secret = config.get('logintwitter', 'consumer_secret')
access_key = config.get('logintwitter', 'access_key')
access_secret = config.get('logintwitter', 'access_secret')


consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret) #twitter: sign me in
access_token = oauth.Token(key=access_key, secret=access_secret) #grant me access
client = oauth.Client(consumer, access_token) #object return

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data) #take a JSON string convert it to dictionary structure:
for tweet in tweets:
    print(tweet["text"])