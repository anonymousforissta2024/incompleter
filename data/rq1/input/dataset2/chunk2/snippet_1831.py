#Source: https://stackoverflow.com/questions/41004459/nameerror-name-tweets-source-not-defined-but-it-has-default-value
formatter = TweetFormatter('twitter_data.txt')
tweets = formatter.convert2json()