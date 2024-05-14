#Source: https://stackoverflow.com/questions/72978255/typeerror-unsupported-operand-types-for-list-and-list-when-using-quive
import matplotlib.pyplot as plt

x1 = [ 0.5, 0.6, 0.3, 0.2 ]
x2 = [ 0.5, 0.6, 0.3, 0.2 ]
x3 = [ 0.2, 0.3, 0.5, 0.6 ]
x4 = [ 0.4, 0.3, 0.2, 0.1 ]

y1 = [ 0.7, 0.9, 0.1, 0.2 ]
y2 = [ 0.8, 0.5, 0.9, 0.2 ]
y3 = [ 0.6, 0.9, 0.1, 0.2 ]
y4 = [ 0.8, 0.2, 0.3, 0.5 ]

deltaX1, deltaX2, deltaX3, deltaX4 = [x[1:] - x[:-1] for x in [x1, x2, x3, x4]]
deltaY1, deltaY2, deltaY3, deltaY4 = [y[1:] - y[:-1] for y in [y1, y2, y3, y4]]

line1 = plt.plot(x1, y1,'bo-',label='apple') 
line2 = plt.plot(x2, y2,'go-',label='banana') 
line3 = plt.plot(x3, y3,'ko-',label='orange')
line4 = plt.plot(x4, y4,'ro-',label='tomato') 

arrows1 = plt.quiver(x1[:-1], y1[:-1], deltaX1, deltaY1, scale_units='xy', angles='xy', scale=1)
arrows2 = plt.quiver(x2[:-1], y2[:-1], deltaX2, deltaY2, scale_units='xy', angles='xy', scale=1)
arrows3 = plt.quiver(x3[:-1], y3[:-1], deltaX3, deltaY3, scale_units='xy', angles='xy', scale=1)
arrows4 = plt.quiver(x4[:-1], y4[:-1], deltaX4, deltaY4, scale_units='xy', angles='xy', scale=1)


plt.title("Fruits")
plt.ylabel("Tastiness")
plt.xlabel("Benefit")

plt.legend(bbox_to_anchor=(1.5, 1),
           bbox_transform=plt.gcf().transFigure)