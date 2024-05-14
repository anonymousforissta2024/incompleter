#Source: https://stackoverflow.com/questions/60087408/python-pandas-and-nltk-type-error-int-object-is-not-callable-when-calling-a
import pandas as pd
import numpy as np
import nltk
import string
import collections
from collections import Counter
nltk.download('stopwords')
sw= set(nltk.corpus.stopwords.words ('english'))
punctuation = set (string.punctuation)
data= pd.read_csv('~/Desktop/tweets.csv.zip', compression='zip')

print (data.columns)
print (len(data.tweet_id))
tweets = data.text
test = pd.DataFrame(data)
test.column = ["text"]
# Exclude stopwords with Python's list comprehension and pandas.DataFrame.apply.
test['tweet_without_stopwords'] = test['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (sw) and word for word in x.split() if word not in punctuation]))
print(test)
chirps = test.text
splitwords = [ nltk.word_tokenize( str(c) ) for c in chirps ]
allWords = []
for wordList in splitwords:
    allWords += wordList
allWords_clean = [w.lower () for w in allWords if w.lower () not in sw and w.lower () not in punctuation]   
tweets2 = pd.Series(allWords)

words = nltk.FreqDist(tweets2)