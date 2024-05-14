#Source: https://stackoverflow.com/questions/59063220/typeerror-expected-string-or-bytes-like-object-while-trying-to-plot-data-from-a
path = '/Users/pradeepallath/Documents/000_Edureka_Training/001_PredictiveAnalysis/Weather_WWII'
import pandas as pd
dataset = pd.read_csv(path+'/Weather.csv',low_memory=False,nrows=1000)
dataset.plot(x='MinTemp',y='MaxTemp',style=0)
plt.plot()