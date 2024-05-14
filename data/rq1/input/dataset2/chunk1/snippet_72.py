#Source: https://stackoverflow.com/questions/46618669/i-am-using-gridsearchcv-and-fit-is-giving-me-a-typeerror-get-params-missing-1
k=['rbf', 'linear','poly','sigmoid']
c= [1,5,10,20,30,50,80,100]
g=[1e-7,1e-6,1e-5,1e-4,1e-2,0.0001]

param_grid=dict(kernel=k, C=c, gamma=g)
print (param_grid)
grid = GridSearchCV(SVC, param_grid,scoring='accuracy')
grid.fit(X_t_train, y_t_train)  

print()
print("Grid scores on development set:")
print()  
print (grid.grid_scores_)
print("Best parameters set found on development set:")
print()
print(grid.best_params_)
print("Grid best score:")
print()
print (grid.best_score_)