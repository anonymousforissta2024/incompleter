#Source: https://stackoverflow.com/questions/53911591/pythontypeerror-cant-multiply-sequence-by-non-int-of-type-list
def polynomial_features(data, deg):
    data_copy=data.copy()
    #print(data_copy.head())
    for i in range(1,deg):
        data_copy['X'+str(i+1)]=data_copy['X'+str(i)]*data_copy['X1']
    return data_copy

x_pred = pd.Series({'X1':[i/200.0 for i in range(200)]})
y_pred = model.predict(polynomial_features(x_pred,deg))