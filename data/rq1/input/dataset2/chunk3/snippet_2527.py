#Source: https://stackoverflow.com/questions/65529910/nameerror-name-predicted-is-not-defined-while-using-google-colab
from google.colab import drive

drive.mount('/content/drive')

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)

import sys
sys.path.append('/content/drive/MyDrive/Colab Notebooks')
from knn import KNN
clf = KNN(k=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
acc = np.sum(predictions == y_test) / len(y_test)
print(acc)