#Source: https://stackoverflow.com/questions/64636058/attributeerror-line2d-object-has-no-property-cmap
#create x,y coordinates
x = numpy.random.choice(10,10)
y = numpy.random.choice(10,10)

#create an array of colors based on direction of line (0=r, 1=g, 2=b)
colors = []
#create an array that is one position away from original 
#to determine direction of line 
yCopy = list(y[1:])
for y1,y2 in zip(y,yCopy):
    if y1 > y2:
        colors.append(0)
    elif y1 < y2:
        colors.append(1)
    else:
        colors.append(2)
#add tenth spot to array as loop only does nine
colors.append(2)

#create a numpy array of colors
categories = numpy.array(colors)

#create a color map with the three colors
colormap = numpy.array([matplotlib.colors.colorConverter.to_rgb('r'),matplotlib.colors.colorConverter.to_rgb('g'),matplotlib.colors.colorConverter.to_rgb('b')])

#plot line
matplotlib.axes.plot(x,y,color=colormap[categories])