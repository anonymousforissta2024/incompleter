#Source: https://stackoverflow.com/questions/52989405/attributeerror-when-scoring-sklearn-pipeline-with-custom-transformer-subclass-bu
from sklearn.datasets import make_regression
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

X, y = make_regression() #Just some dummy regression data for demonstrative purposes.

class BaseTransformer(TransformerMixin, BaseEstimator):

    def __init__(self):
        print("Base Init")

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        return X

class DerivedTransformer(BaseTransformer):

    def __init__(self):
        super(DerivedTransformer, self).__init__()
        print("Dervied init")

    def fit(self, X, y = None):
        super(DerivedTransformer, self).fit(X, y)
        self.new_attribute = 0.0001
        return self

    def transform(self, X):
        output = super(DerivedTransformer, self).transform(X)
        output += self.new_attribute

        return output

base_pipeline = Pipeline([('base_transformer', BaseTransformer()),
              ('linear_regressor', LinearRegression())])

derived_pipeline = Pipeline([('derived_transformer', DerivedTransformer()),
              ('linear_regressor', LinearRegression())])