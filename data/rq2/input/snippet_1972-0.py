import numpy

def colsum(arr, n, m):
    for i in range(n):
        su = 0
        for j in range(m):
            su += arr[j][i]
        print(su, end=' ')
TwoDArray = numpy.array(TwoDList)
print('2D Array:')
print(TwoDArray)
print('\nColumn-wise Sum:')
colsum(TwoDArray, len(TwoDArray[0]), len(TwoDArray))