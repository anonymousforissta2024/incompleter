#Source: https://stackoverflow.com/questions/23319266/using-numpy-genfromtxt-gives-typeerror-cant-convert-bytes-object-to-str-impl
from pandas import read_csv
import numpy as np
from sklearn.linear_model.stochastic_gradient import SGDClassifier
from sklearn import preprocessing
import sklearn.metrics as metrics
from sklearn.cross_validation import train_test_split

#d = pd.read_csv("data.csv", dtype={'A': np.str(), 'B': np.str(), 'S': np.str()})

dataset = np.genfromtxt(open('data.csv','r'), delimiter=',', dtype='f8')[1:]
target = np.array([x[19] for x in dataset])
train = np.array([x[1:] for x in dataset])

print(target)