#Source: https://stackoverflow.com/questions/70836134/mlp-regression-error-typeerror-not-supported-between-instances-of-numpy
mlp = MLPRegressor()
parameter_space = {
    'max_iter': [1000,2000,5000],
    'activation': ['relu'],
    'alpha': [0.0001,0.001,0.01],
    'hidden_layer_sizes': [(8,8,),(50,50,),(100,100,)],
    'solver': ['sgd', 'adam'],
    'learning_rate': ['constant','adaptive']
}
k = 5
kf = KFold(n_splits=k, random_state=None)
model = MLPRegressor(parameter_space)
acc_score = []
for train_index , test_index in kf.split(x):
    x_train , x_valid = x[train_index,:],x[test_index,:]
    y_train , y_valid = y[train_index] , y[test_index]
    model.fit(x_train[1:50], y_train[1:50])