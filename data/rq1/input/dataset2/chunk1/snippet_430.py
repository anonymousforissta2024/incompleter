#Source: https://stackoverflow.com/questions/36961007/typeerror-unsupported-operand-types-for-nonetype-and-int
def calculatePerimeter(length, depth):
    if depth == 1:
        return 3 * length
    else:
        print (calculatePerimeter(length, depth-1) * (4/3)**(depth)) / ((4/3)**(depth-1))

calculatePerimeter(100, 3)