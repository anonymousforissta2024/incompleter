#Source: https://stackoverflow.com/questions/49762971/attributeerror-tuple-object-has-no-attribute-lower
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
text_train_cv = cv.fit_transform(train)
text_train_cv.shape