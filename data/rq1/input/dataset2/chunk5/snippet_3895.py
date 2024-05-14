#Source: https://stackoverflow.com/questions/57917397/i-get-this-type-of-error-typeerror-not-supported-between-instances-of-in
from sklearn.preprocessing import LabelEncoder
var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area']
le = LabelEncoder()
for i in var_mod:
    data[i] = le.fit_transform(data[i])