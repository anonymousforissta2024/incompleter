#Source: https://stackoverflow.com/questions/52726959/i-have-a-problem-with-this-error-message-typeerror-unsupported-operand-types
testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)