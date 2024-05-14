#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder

ct  = ColumnTransformer(transformers = [('encoder', OneHotEncoder() , [3])], remainder = 'passthrough')

x = np.array(ct.fit_transform(x))

print(x)