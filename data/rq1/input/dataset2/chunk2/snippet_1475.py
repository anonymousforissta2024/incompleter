#Source: https://stackoverflow.com/questions/75243740/attributeerror-tuple-object-has-no-attribute-sum
import matplotlib.pyplot as plt
import numpy

labels = 'Updated', 'Coverage (overall)', 'last 24 hours', 'Deleted', 'Deleted last 24 hours', 'Banned', 'Banned last 24 hours'
sizes = (6, 5.04, 0, 12, 0, 7, 7)
colors = ['yellowgreen', 'gold', 'lightskyblue', 'green', 'black', 'red', 'grey']

def absolute_value(val):
    a  = numpy.round(val/100.*sizes.sum(), 0)
    return a

plt.pie(sizes, labels=labels, colors=colors,
        autopct=absolute_value)

plt.axis('equal')
plt.show()