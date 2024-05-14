#Source: https://stackoverflow.com/questions/35996970/typeerror-fit-missing-1-required-positional-argument-y
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.cross_validation import train_test_split
X = data
Y = target
model = GaussianNB
X_train, X_test, Y_train, Y_test = train_test_split(X,Y)
model.fit(X_train, Y_train)