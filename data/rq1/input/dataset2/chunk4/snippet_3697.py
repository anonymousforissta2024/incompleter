#Source: https://stackoverflow.com/questions/51320783/python-3-6-tkinter-not-finding-file-filenotfounderror-errno-2-no-such-fil
import matplotlib.animation as animation

def animate(i):
    pullData = open('sampleData.csv', "r").read()
    dataList = pullData.split('\n')
    xList =[]
    yList = []
    for eachLine in dataList:
        if len(eachLine)>1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear()
    a.plot(xList, yList )