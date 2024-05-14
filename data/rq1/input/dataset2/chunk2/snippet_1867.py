#Source: https://stackoverflow.com/questions/69653835/attribute-error-pickle-load-seldon-deployment
from sklearn.preprocessing import LabelEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

class MyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        df = X
        vars_cat = [var for var in df.columns if df[var].dtypes == 'O']
        cat_with_na = [var for var in vars_cat if df[var].isnull().sum() > 0]
        df[cat_with_na] = df[cat_with_na].fillna('Missing')

        return df