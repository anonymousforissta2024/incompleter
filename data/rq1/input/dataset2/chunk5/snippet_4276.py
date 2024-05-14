#Source: https://stackoverflow.com/questions/52726959/i-have-a-problem-with-this-error-message-typeerror-unsupported-operand-types
trainingSet=[]
testSet=[]
loadDataset('iris.csv', 0.66, trainingSet, testSet)
print('Train: ' + repr(len(trainingSet))) 
print('Test: ' + repr(len(testSet)))