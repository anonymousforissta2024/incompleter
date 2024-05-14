#Source: https://stackoverflow.com/questions/51125475/typeerror-fit-transform-missing-1-required-positional-argument-x
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = Imputer.fit(imputer,X[:,1:3])
X[:, 1:3] = Imputer.transform(imputer,X[:, 1:3])

#Spliting the dataset into Training set and Test Set
from sklearn.cross_validation import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)

#Feature Scalling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)