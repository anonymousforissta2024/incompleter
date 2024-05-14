#Source: https://stackoverflow.com/questions/54171455/how-to-fix-the-typeerror-g-must-be-a-d-matrix
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import cvxpy

X, y = make_classification(n_samples=1000, n_features=20, n_classes=8,n_informative=5,
                           class_sep=0.2, random_state=2)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=1)

model = RandomForestClassifier(random_state=1)
model.fit(X_train, y_train)
test_probs = model.predict_proba(X_test)

#clipping so that we don't take log of 0 or 1
test_probs = np.clip(test_probs, 0.0001, 0.9999)

#turning into costs
model_costs = -np.log10(test_probs)

# Our allocation cannot exceed our supply
# 150 flyers, 80 pamphlets, 25 bumper stickers
supply = np.atleast_2d([150, 80, 25])

# Creating our cvxpy variable of assignments
selection = cvxpy.Bool(*test_probs.shape)

# Constant matrix that counts how many of each 
# material we sent to each constituent
TRANSFORMER = np.array([[1,0,0],
                        [0,1,0],
                        [0,0,1],
                        [1,1,0],
                        [1,0,1],
                        [0,1,1],
                        [1,1,1],
                        [0,0,0]])

supply_constraint = cvxpy.sum_entries(selection * TRANSFORMER, axis=0) <= supply

# We must make our choice per constituent
# remember that the last column is for "no materials"
feasibility_constraint = cvxpy.sum_entries(selection, axis=1) == 1
constraints = [supply_constraint, feasibility_constraint]

# Take the negative log of our probabilities to turn them into costs
cost = cvxpy.sum_entries(cvxpy.mul_elemwise(model_costs, selection))

# Solving the problem
problem = cvxpy.Problem(cvxpy.Minimize(cost), constraints=constraints)
problem.solve(solver=cvxpy.GLPK_MI)