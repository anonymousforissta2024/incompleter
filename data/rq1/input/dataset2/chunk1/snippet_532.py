#Source: https://stackoverflow.com/questions/58131330/solving-attributeerror-while-loading-tfidfvectorizer-with-pickle
import pickle

vectorizer = TfidfVectorizer(...)
doc_mat = vectorizer.fit_transform(corpus)
with open("vectorizer.pickle", "wb") as f:
    pickle.dump(vectorizer, f)

with open("docmat.pickle", "wb") as f:
    pickle.dump(doc_mat, f)