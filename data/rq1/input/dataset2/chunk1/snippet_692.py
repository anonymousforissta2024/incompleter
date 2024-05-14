#Source: https://stackoverflow.com/questions/58131330/solving-attributeerror-while-loading-tfidfvectorizer-with-pickle
import pickle

# This load generates the error below
with open("vectorizer.pickle", 'rb') as f:
    vectorizer = pickle.load(f)

# This load works:
with open("docmat.pickle", 'rb') as f:
    doc_mat = pickle.load(f)