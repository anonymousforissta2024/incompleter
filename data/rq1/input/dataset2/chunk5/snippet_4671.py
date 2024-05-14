#Source: https://stackoverflow.com/questions/48377146/typeerror-numpy-ndarray-object-is-not-callable-in-my-code
import numpy as np
import csv

x = np.genfromtxt("boston_housing.csv",dtype=float,delimiter=',',skip_header=1,usecols = (0,1,2,3,4,5,6,7,8,9,10,11,12))
xx = x
y = np.genfromtxt("boston_housing.csv",dtype=float,delimiter=',',skip_header=1,usecols = (13))

"""
ave = np.zeros(13)
sum = np.zeros(13)
mn = [x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5],x[0][6],x[0][7],x[0][8],x[0][9],x[0][10],x[0][11],x[0][12]]
mx = [x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],x[0][5],x[0][6],x[0][7],x[0][8],x[0][9],x[0][10],x[0][11],x[0][12]]
for row in x:
    for i in range(0,13):
        sum[i] = sum[i] + row[i]
        mn[i] = min(mn[i],row[i])
        mx[i] = max(mx[i],row[i])
"""
alpha = 0.001
theta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for ll in range(0,1):
    temp = []
    grad0 = (1.0/506)*sum([(theta[0] + theta[1]*xx[i][0] + theta[2]*xx[i][1] + theta[3]*xx[i][2] + theta[4]*xx[i][3] + theta[5]*xx[i][4] + theta[6]*xx[i][5]
                        + theta[7]*xx[i][6] + theta[8]*xx[i][7] + theta[9]*xx[i][8] + theta[10]*xx[i][9] + theta[11]*xx[i][10] + theta[12]*xx[i][11]
                        + theta[13]*xx[i][12] - y[i]) for i in range (506)])
    temp.append(theta[0] - (alpha * grad0))
    for j in range(1,14):
        grad0 = (1.0/506)*sum([(theta[0] + theta[1]*xx[i][0] + theta[2]*xx[i][1] + theta[3]*xx[i][2] + theta[4]*xx[i][3] + theta[5]*xx[i][4] + theta[6]*xx[i][5]
                            + theta[7]*xx[i][6] + theta[8]*xx[i][7] + theta[9]*xx[i][8] + theta[10]*xx[i][9] + theta[11]*xx[i][10] + theta[12]*xx[i][11]
                            + theta[13]*xx[i][12] - y[i])*xx[i][j-1] for i in range (506)])
        temp.append(theta[j] - (alpha * grad0))
    theta = temp
yy = [0.02501,35,4.15,1,0.77,8.78,81.3,2.5051,24,666,17,382.8,11.48]
ans = 0
for i in range(0,13):
    ans = ans + (yy[i] * theta[i+1])
ans = ans + theta[0]
print(theta)
print(ans)