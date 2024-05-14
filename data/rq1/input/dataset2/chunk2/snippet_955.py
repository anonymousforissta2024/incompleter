#Source: https://stackoverflow.com/questions/52421840/bar-plot-with-color-gradient-on-each-bar-error-typeerror-object-of-type-list
import matplotlib.pyplot as plt
quiz=[1,2,0,4,8,10]
plt.barh(range(len(quiz)), quiz, align='center', alpha=0.5, color='blue')