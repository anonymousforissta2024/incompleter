#Source: https://stackoverflow.com/questions/50435311/program-is-not-working-typeerror-fit-missing-1-required-positional-argument
from sklearn import tree
from sklearn.datasets import load_iris
iris=load_iris()
dir(iris)
#output data to traixn setosa,versicolor and virginica
x=iris.data
#fetching data
x=np.delete(x, np.s_[::50], 0)
#print(x)
y=iris.target
#featching output
y=np.delete(y, np.s_[::50], 0)
algo=tree.DecisionTreeClassifier