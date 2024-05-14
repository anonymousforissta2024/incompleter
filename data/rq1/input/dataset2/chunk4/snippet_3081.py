#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train ,y_train)