#Source: https://stackoverflow.com/questions/76129300/typeerror-unhashable-type-csr-matrix-encoding-categorical-data-to-make-a-m
#importing the dataset 
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, -1].values


#Encoding categorical data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
enc = OneHotEncoder()
X[:, :-1] = enc.fit_transform(X[:, :-1])

X = enc.fit_transform(X).toarray() 
# Avoiding the Dummy Variable Trap
X = X[:, 1:]