#Source: https://stackoverflow.com/questions/55661668/attributeerror-get-numeric-data-iris-dataset
import pandas as pd
import numpy
import mglearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iri = load_iris()

xTrain, xTest, yTrain, yTest = train_test_split(iri['data'], iri['target'], random_state=0)

print(xTrain.shape)

iriFrame = pd.DataFrame(xTrain, columns=iri.feature_names)
pd.plotting.scatter_matrix(iri, c=yTrain, figsize=(15, 15), marker='o', hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)
#print('Keys: \n{}'.format(iri.keys()))
#print(iri['data'])
#print(iri['feature_names'])