#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

print(x_train)

print(x_test)

print(y_train)

print(y_test)