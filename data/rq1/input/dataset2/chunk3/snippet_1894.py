#Source: https://stackoverflow.com/questions/59905138/python-error-typeerror-fit-missing-2-required-positional-arguments-x-and
from sklearn import tree

#[height,weight,shoe size]

X = [181,80,44], [177,70,43], [160,60,38], [154, 54,37]

Y = ['male','female','female','female']

clf = tree.DecisionTreeClassifier

clf = clf.fit(X,Y)

prediciton = clf.predict([[190,70,43]])

'print'(prediciton)