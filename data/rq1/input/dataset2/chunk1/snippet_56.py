#Source: https://stackoverflow.com/questions/57577132/python-3-7-attributeerror-list-object-has-no-attribute-split
analyser = SentimentIntensityAnalyzer()

def print_sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(snt)))


print_sentiment_scores(your_list)