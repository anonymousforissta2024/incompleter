#Source: https://stackoverflow.com/questions/47081700/fitting-tfidfvectorizer-attributeerror-typeerror
import nltk
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Make tokens per line

dataset = pd.read_csv('Cleansed Data.csv', delimiter=';', encoding='latin1')
tokens = dataset['Description'].apply(nltk.word_tokenize)
tokens_line = pd.DataFrame(np.array(tokens).reshape(len(tokens), 1), 
columns=['tokens'])
tokens_line_lists = tokens_line.values.tolist()    

# Get unique tokens

Filename = open('descriptions for tokens.txt')
vectorizer = CountVectorizer()
dtm = vectorizer.fit_transform(Filename)
vocab = vectorizer.get_feature_names()
tokens_unique = pd.DataFrame(np.array(vocab).reshape(len(vocab), 1), 
columns=['tokens'])

#TF-IDF Vectoriser

tfidf_vectoriser = TfidfVectorizer(max_df=0.8, max_features=20000, 
min_df=0.2, use_idf=True, tokenizer=tokens_unique, ngram_range=(1,3))

tfidf_matrix = tfidf_vectoriser.fit_transform(tokens_line)