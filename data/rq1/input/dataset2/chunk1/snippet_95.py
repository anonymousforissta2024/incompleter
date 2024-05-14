#Source: https://stackoverflow.com/questions/54974905/attributeerror-numpy-ndarray-object-has-no-attribute-target
#Grid Search Parameter Tuning
import numpy as np
from sklearn import datasets
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# datasets
dataset = np.random.rand(1000,2)

#Ridge regression 
alphas = np.array([1,0.1,0.01,0.001,0.0001,0])
model = Ridge()
grid = GridSearchCV(estimator=model, param_grid=dict(alpha=alphas))
grid.fit(dataset.data, dataset.target)