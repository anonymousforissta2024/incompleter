#Source: https://stackoverflow.com/questions/52749012/python-typeerror-1-is-not-a-string
xw = 1
xmin = data['xmin']
ymin = data['ymin']
ymax = data['ymax']

plt.figure()
list(map(lambda x,y,z:plt.broken_barh([(x,xw)], (y, z), facecolors = 'blue'), xmin,ymin,ymax))