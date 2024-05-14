#Source: https://stackoverflow.com/questions/53765719/filenotfounderror-in-python-during-arabic-text-analysis
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [open(f) for f in text_files]
tfidf = TfidfVectorizer().fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
pairwise_similarity = tfidf * tfidf.T