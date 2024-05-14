#Source: https://stackoverflow.com/questions/50119091/typeerror-unhashable-type-list-in-python-nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re

fo = open('cran.all.1400', 'r+')
contents = fo.read()
docs = re.split(r'\.I[\s][\d]*')

stop_words = set(stopwords.words('english'))

tokens = []
for each in docs:
    tokens.append(word_tokenize(eac))

s_words = [w for w in tokens if not w in stop_words]
print(s_words)