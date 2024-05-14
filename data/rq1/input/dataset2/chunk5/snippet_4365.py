#Source: https://stackoverflow.com/questions/77465161/attributeerror-numpy-ndarray-object-has-no-attribute-columns-when-i-didn
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

class Cleaner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = X.drop(["Name", "PassengerId", "FoodCourt", "ShoppingMall", "Cabin"], axis=1)
        return X

class ObjectEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        columns_to_encode = ["HomePlanet", "CryoSleep", "Destination", "VIP"]
        encoder = OneHotEncoder()
        
        # Encode each attribute and add the columns to the DataFrame
        for column in columns_to_encode:
            matrix = encoder.fit_transform(X[[column]]).toarray()
            column_names = [f"{column}_{i}" for i in range(matrix.shape[1])]
        
            for i in range(len(matrix.T)):
                X[column_names[i]] = matrix.T[i]

        # Remove Old Parameters
        X = X.drop(["HomePlanet", "CryoSleep", "Destination", "VIP"], axis=1)

        return X

class LabelYEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)
        return y_encoded

class NullImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        features_with_missing_values = X.columns[X.isnull().any()].tolist()
        imputer = SimpleImputer(strategy='median')
        X[features_with_missing_values] = imputer.fit_transform(X[features_with_missing_values])
        return X

pipeline = Pipeline([
    ("cleaner", Cleaner()),
    ("object_encoder", ObjectEncoder()),
    ("label_y_encoder", LabelYEncoder()),
    ("null_imputer", NullImputer()),
])
X = pipeline.fit_transform(strat_train_set)