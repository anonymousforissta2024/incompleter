#Source: https://stackoverflow.com/questions/74920325/dtreeviz-attributeerror-dataframe-object-has-no-attribute-dtype-python
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from dtreeviz.trees import *


#fit the classifier
clf = tree.DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)