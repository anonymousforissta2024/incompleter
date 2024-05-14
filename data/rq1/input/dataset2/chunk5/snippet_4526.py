#Source: https://stackoverflow.com/questions/68197818/typeerror-all-intermediate-steps-should-be-transformers-and-implement-fit-and-t
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from imblearn.pipeline import make_pipeline
num_pipline = Pipeline([
    ('imputer', SimpleImputer(missing_values=np.nan, strategy='median')),
    ('attribs_adder', CombineAttributesAdder(add_bedrooms_per_room=False)),
    ('stand_scaler', StandardScaler()),
])
housing_num_transform = num_pipline.fit_transform(housing_num)