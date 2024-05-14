#Source: https://stackoverflow.com/questions/57585725/typeerror-init-got-an-unexpected-keyword-argument-param-distributions
grdHyperParams = {'loss' : ['deviance', 'exponential'],
                 'n_estimators': randint(10, 500),
                 'max_depth': randint(1,10)}

gridSearch_grd = GridSearchCV(estimator=grd, param_distributions=grdHyperParams, n_iter=10, scoring='roc_auc',fit_params=None, cv=None, 
verbose=2).fit(X3_train, y_train)