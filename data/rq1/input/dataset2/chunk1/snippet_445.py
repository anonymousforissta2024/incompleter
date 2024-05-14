#Source: https://stackoverflow.com/questions/65172406/typeerror-qpixmap-argument-1-has-unexpected-type-figure
import matplotlib.pyplot as plt
import numpy as np

labels = ['Word', 'Excel', 'Chrome','Visual Studio Code'] 
title = [20,32,22,25] 
cores = ['lightblue','green','blue','red']
explode = (0,0.1,0,0)
plt.rcParams['font.size'] = '16'
total=sum(title)
plt.pie(title,explode=explode,labels=labels,colors=cores,autopct=lambda p: '{:.0f}'.format(p*total/100), shadow=True, startangle=90)
plt.axis('equal')
grafic = plt.gcf()
self.ui.grafig_1.setPixmap(QPixmap(grafic))