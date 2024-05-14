#Source: https://stackoverflow.com/questions/57601970/name-error-when-declaring-a-2d-array-inside-a-class
class HelloWorld:
    rows = 5
    cols = 5
    arr = [[0 for i in range(cols)] for j in range(rows)]