#Source: https://stackoverflow.com/questions/30230380/attributeerror-str-object-has-no-attribute-words
from textblob import TextBlob as tb
import math

words={}
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(words, bloblist)))

bloblist = open('afterstopwords.csv', 'r').read()

for i, blob in enumerate(bloblist):
     print("Top words in document {}".format(i + 1))
     scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
     sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
     for word, score in sorted_words[:3]:
         print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))