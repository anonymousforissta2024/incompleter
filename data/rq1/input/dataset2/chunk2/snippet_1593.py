#Source: https://stackoverflow.com/questions/52731818/typeerror-issue-with-gridsearchcv
parameter={'svm_C':(0.1, 1, 10, 100), 'svm_gamma':(0.001, 0.01, 0.1, 10)}
pipe=Pipeline([("scaler", StandardScaler), ("svm", SVC())])
print(parameter)
print(pipe)

print(xtrain.shape)
print(ytrain1.shape)
grid=GridSearchCV(pipe, parameter, cv=3, n_jobs=-1)
grid.fit(xtrain,ytrain1)
print("Best set score:{}".format(grid.best_score_))
print("Test set Score:{}".format(grid.score(xtest,ytest1)))
print("Best paameters:{}".format(grid.best_params_))
filename='finalized_svm.sav'
filename1='gridfinal_svm.sav'
joblib.dump(best_estimator_, filename)
joblib.dump(grid, filename1)
pred=grid.predict(xtest)
confusion=confusion_matrix(ytest1,pred), print(confusion)