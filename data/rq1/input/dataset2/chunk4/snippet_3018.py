#Source: https://stackoverflow.com/questions/71716965/how-can-i-fix-this-attributeerror-module-numbers-has-no-attribute-integral
import matplotlib.pyplot as plt

fileobj = open('marchweatherfull.csv', 'r')
data = fileobj.readlines()
fileobj.close()

mins = [] # do the same for maxs, nines and threes
maxs = []
nines = []
threes = []

for line in data:
    splitline = line.split(',')
    mins.append(float(splitline[2]))
    maxs.append(float(splitline[3]))
    nines.append(float(splitline[10]))
    threes.append(float(splitline[16]))

dates = [d for d in range(1,32)]
plt.plot(dates, mins, dates, maxs, dates, nines, dates, threes)
plt.show()


print(mins)