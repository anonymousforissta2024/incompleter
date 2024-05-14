#Source: https://stackoverflow.com/questions/62590974/scikit-learn-pipeline-preprocessing-with-typeerror-not-supported-between-in
from sklearn.pipeline import make_pipeline, Pipeline
from mlxtend.preprocessing import DenseTransformer

numeric_features=X.select_dtypes(include=['int64', 'float64']).columns
numeric_transformer=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='median')),
    ('scaler',StandardScaler())])

categorical_features=X.select_dtypes(include=['object']).columns
categorical_transformer=Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='constant',fill_value='missing')),
    ('onehot',OneHotEncoder(handle_unknown='ignore')),
    ('to_dense', DenseTransformer())])

preprocessor=ColumnTransformer(transformers=[
    ('num',numeric_transformer,numeric_features),
    ('cat',categorical_transformer,categorical_features)])

from sklearn.ensemble import RandomForestClassifier
rf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', RandomForestClassifier())])
rf.fit(X_train1, Y_train1) #--> this is when the error message points to