#Source: https://stackoverflow.com/questions/74989743/how-can-i-choose-a-specific-intersection-element-in-a-list-typeerror-unhashed
#x = []
#x.append([[hockeymatch], [number1], [number2]])
x = [[[('Dallas-Arizona', 'NHL', '15:00')], [1.75], [87.5]],
     [('Seattle-Minnesota', 'NHL', '18:00')], [2.5], [125.0]]

#y = []
#y.append([[hockeymatch], [number1], [number2]])
y = [[[('Seattle-Minnesota', 'NHL', '18:00')], [1.33], [62.0]],
       [('Vancouver-Vegas', 'NHL', '20:00')], [0.50], [43.0]]

test = list(set(x[0]).intersection(y[0]))
print(test)