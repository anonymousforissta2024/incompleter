#Source: https://stackoverflow.com/questions/60293801/typeerror-float-argument-must-be-string-or-number-not-novaluetype
import matplotlib.pyplot as plt

x = [1, 2, 3]

y = [2, 4, 1]

plt.plot(x, y)

plt.xlabel('X - axis')

plt.ylabel('y - axis')

plt.title('My first graph')

plt.show()