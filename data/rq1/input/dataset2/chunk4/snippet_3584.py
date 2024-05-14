#Source: https://stackoverflow.com/questions/77095936/nameerror-name-np-array-is-not-defined
import numpy as np
def y_true():
    np_array= np. add(y_true,y_pred)

no_of_pred =24
ind=72
y_pred= forecast(x_val,no_of_pred,ind)
y_true = y_val[ind:ind+(no_of_pred)]

# Lets convert back the normalized values to the original dimensional space
y_true = np_array.reshape(1, -1)
y_true= y_scaler.inverse_transform(y_true)

y_pred = np_array.reshape(1, -1)
y_pred= y_scaler.inverse_transform(y_pred)