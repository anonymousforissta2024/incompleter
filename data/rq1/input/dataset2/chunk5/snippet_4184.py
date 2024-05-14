#Source: https://stackoverflow.com/questions/52726959/i-have-a-problem-with-this-error-message-typeerror-unsupported-operand-types
data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, 3)
print('Distance: ' + repr(distance))