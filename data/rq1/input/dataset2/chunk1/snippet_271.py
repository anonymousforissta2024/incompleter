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
print(data.text)
data['text'] = [str.lower () for str in data.text if str.lower () not in sw and str.lower () not in punctuation] 
print(data.text)
data["text"] = data["text"].str.split()
data['text'] = data['text'].apply(lambda x: [item for item in x if item not in sw])
print(data.text)
data['text'] = data.text.astype(str)
print(type(data.text))
tweets=data.text

data['words']= tweets.apply(nltk.FreqDist(tweets))
print(data.words)