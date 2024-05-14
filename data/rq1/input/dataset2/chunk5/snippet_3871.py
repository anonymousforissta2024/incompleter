#Source: https://stackoverflow.com/questions/49869413/python-list-comprehension-with-zip-typeerror-numpy-float64-object-cannot-be
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('/iris1.csv')
df = pd.DataFrame(data)

X=df.iloc[:,0:4]
y=df.iloc[:,4]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Calculate Error Rate
def calc_error_rate(pred, Y):
    return sum(pred != Y) / float(len(Y))


def AdaBoost(y_train, X_train, y_test, X_test, M, clf):

    n_train = len(X_train)
    n_test = len(X_test)

    # Initialize weights
    w = np.ones(n_train) / n_train


    pred_train = np.zeros(n_train)
    pred_test = np.zeros(n_test)

    for i in range(M):

    # Fit a classifier with the specific weights
        clf.fit(X_train, y_train, sample_weight = w)
        pred_train_i = clf.predict(X_train)
        pred_test_i = clf.predict(X_test)

        # Indicator function
        miss = [int(x) for x in (pred_train_i != y_train)]

        # Equivalent with 1/-1 to update weights
        miss2 = [x if x==1 else -1 for x in miss]

        # Compute the error
        err_m = np.dot(w,miss) / sum(w)

        # wi
        wi = 0.5 * np.log( (1 - err_m) / float(err_m))

        # New weights
        w = np.multiply(w, np.exp([float(x) * wi for x in miss2]))

        # Add to prediction
        pred_train = [sum(x) for x in zip(pred_train, [x * wi for x in pred_train_i])]
        pred_test = [sum(x) for x in zip(pred_test, [x * wi for x in pred_test_i])]

    pred_train = np.sign(pred_train)
    pred_test = np.sign(pred_test)

    # Return error rate in train and test set
    return calc_error_rate(pred_train, y_train), calc_error_rate(pred_test, y_test)

# Use the Decision Tree Classifier for model, M
clf_tree = DecisionTreeClassifier()

x_range = range(1, 500, 1)

for i in x_range:    
    classifier = AdaBoost(y_train, X_train, y_test, X_test, i, clf_tree)