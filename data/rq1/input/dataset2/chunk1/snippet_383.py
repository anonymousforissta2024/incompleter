#Source: https://stackoverflow.com/questions/67552839/kds-library-gives-attributeerror-module-kds-has-no-attribute-metrics
# REPRODUCABLE EXAMPLE
# Load Dataset and train-test split
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33,random_state=3)
clf = tree.DecisionTreeClassifier(max_depth=1,random_state=3)
clf = clf.fit(X_train, y_train)
y_prob = clf.predict_proba(X_test)

# The magic happens here
import kds
kds.metrics.report(y_test, y_prob)