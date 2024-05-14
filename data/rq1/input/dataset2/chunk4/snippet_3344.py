#Source: https://stackoverflow.com/questions/67260107/attributeerror-module-matplotlib-cbook-has-no-attribute-check-in-list
import pandas as pd
import matplotlib.pyplot as plt

df['Month'] = pd.to_datetime(df['Month'], infer_datetime_format = True)
df = df.set_index('Month',inplace=False)    
# plot graph
plt.xlabel('date')
plt.ylabel('trafic flow count')
plt.plot(df)