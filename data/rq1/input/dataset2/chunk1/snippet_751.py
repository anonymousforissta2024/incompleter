#Source: https://stackoverflow.com/questions/52816850/typeerror-nonetype-object-is-not-subscriptable-about-lists
import csv
from statistics import mean

averages = list()
sorted_averages = list()
dic = dict()
with open('first.csv') as fopen:
    reader = csv.reader(fopen)
    for line in reader:
        name = line[0]
        line = line[1:]
        counter = 0
        for i in line:
            i = float(i)
            line[counter] = i
            counter += 1
        average = mean(line)
        averages.append(average)
        dic[name] = average
    for i in range(0, len(averages)):
        maxi = 0
        maxi1 = 0
        for number in averages:
            if number > maxi:
                maxi = number
            elif number == maxi:
                maxi = number
                maxi1 = number
            else:
                maxi = maxi
        sorted_averages.append(maxi)
        averages.remove(maxi)
    del(averages)
    insorted_averages = sorted_averages.reverse()
    for z in insorted_averages[:3]:
        print(z)