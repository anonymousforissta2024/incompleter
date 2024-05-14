#Source: https://stackoverflow.com/questions/62465428/typeerror-list-indices-must-be-integers-or-slices-not-float
x = [811.91, 796.04, 796.14, 796.50, 796.81]

i = 0
for i in x:
    difference = x[i+1] - x[i-1]
    print(difference)