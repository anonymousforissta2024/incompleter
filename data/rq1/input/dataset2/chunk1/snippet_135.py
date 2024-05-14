#Source: https://stackoverflow.com/questions/60786220/attributeerror-gridsearchcv-object-has-no-attribute-best-params
from sklearn.model_selection import GridSearchCV
# Create the parameter grid based on the results of random search 
param_grid = {
    'bootstrap': [True],'max_depth': [20,30,40, 100, 110],
    'max_features': ['sqrt'],'min_samples_leaf': [5,10,15],
    'min_samples_split': [40,50,60], 'n_estimators': [150, 200, 250]
}
# Create a based model
rf = RandomForestClassifier()
# Instantiate the grid search model
grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)