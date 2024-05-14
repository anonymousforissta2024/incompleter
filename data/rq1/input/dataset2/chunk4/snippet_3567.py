#Source: https://stackoverflow.com/questions/75197660/python-attributeerror-bool-object-has-no-attribute-any-when-fitting-regres
from sklearn.linear_model import LinearRegression
lm = LinearRegression()

lm.fit(X_train, y_train)