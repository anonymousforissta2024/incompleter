#Source: https://stackoverflow.com/questions/58167836/monte-carlo-integral-typeerror-not-supported-between-instances-of-complex
import random
import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

def montecarlo(functie1,x1,x2,y1,y2): 
    f = functie1(x)
    true_point_x = []
    true_point_y = []
    false_point_x = []
    false_point_y = []
    positive_true = 0 
    negative_true = 0
    n = 100000

    for i in range(n):
        x = (x2-x1) * random.random() + x1
        y = (y2-y1) * random.random() + y1
        if f > 0:
            if y <= f and y > 0:
                true_point_x.append(x)
                true_point_y.append(y)
                positive_true += 1
            else:
                false_point_x.append(x)
                false_point_y.append(y)
                negative_true += 1
        else:
            if y >= f and y < 0:
                true_point_x.append(x)
                true_point_y.append(y)
                positive_true -= 1
            else:
                false_point_x.append(x)
                false_point_y.append(y)
                negative_true += 1

    plt.plot(true_point_x,true_point_y, 'o', markerfacecolor='g', markeredgecolor='k')
    plt.plot(false_point_x,false_point_y, 'o', markerfacecolor='r', markeredgecolor='k')
    plt.show()

    surface = (x2-x1)*(y2-y1)
    integral = surface * positive_true / n
def functie1(x):
    return x ** (x + 0.5)
montecarlo(functie1, -1, 2.2, -1, 1)