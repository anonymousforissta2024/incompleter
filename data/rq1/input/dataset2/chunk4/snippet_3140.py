#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
y_pred = regressor.predict(x_test)

np.set_printoptions(precision=2)

print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))