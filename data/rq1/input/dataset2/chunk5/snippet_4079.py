#Source: https://stackoverflow.com/questions/57211695/importing-modules-results-in-attribute-error
import csv
import seaborn


x = []
y = []

with open('main.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 1
    for row in plots:
        if count % 2 == 1:
            x.append(int(row[0]))
            y.append(int(row[1]))
        count += 1

seaborn.scatterplot(x, y)