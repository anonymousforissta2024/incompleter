#Source: https://stackoverflow.com/questions/66407561/multiplication-of-matrix-in-python3-i-am-using-below-one-line-code-but-i-get-e
from functools import reduce
import operator
def prod(iterable):
    return reduce(operator.mul,iterable,1)
X = [[1,7,3],
    [3,5,8],
    [6,8,9]]
Y = [[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]
resultTranspose=[list(i) for i in zip(*Y)]

result=[[list(map(sum,list(map(prod,zip(i,j))))) for j in resultTranspose]
for i in X]