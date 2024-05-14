#Source: https://stackoverflow.com/questions/61550473/why-does-calling-reversed-upon-a-tuple-throw-an-attribute-error
x = (1, 2, 3, 4)
x.__reversed__()
#causes an attribute error