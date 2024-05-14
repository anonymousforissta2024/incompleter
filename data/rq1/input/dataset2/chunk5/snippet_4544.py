#Source: https://stackoverflow.com/questions/51925123/nameerror-name-fit-classifier-is-not-defined
import pandas as pd
import pandas
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVC
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv('data.csv', encoding = 'utf-8')
data = dataset['text']
labels = dataset['label']

X_train, X_test, y_train, y_test = train_test_split (data, labels, test_size = 0.2, random_state = 0)

count_vector = CountVectorizer()
tfidf = TfidfTransformer()

classifier = OneVsOneClassifier(SVC(kernel = 'linear', random_state = 84))

train_counts = count_vector.fit_transform(X_train)
train_tfidf = tfidf.fit_transform(train_counts)
classifier.fit(train_tfidf, y_train)

test_counts = count_vector.transform(X_test)
test_tfidf = tfidf.transform(test_counts)
classifier.predict(test_tfidf)

fit_classifier(X_train, y_train)
predicted = predict(X_test)

print("confusion matrix")
print(confusion_matrix(X_test, predicted, labels = labels))

print("cross validation")
test_counts = count_vector.fit_transform(data)
test_tfidf = tfidf.fit_transform(test_counts)

scores = cross_validation.cross_val_score(classifier, test_tfidf, labels, cv = 10)
print(scores)
print("Accuracy: {} +/- {}".format(scores.mean(), scores.std() * 2))