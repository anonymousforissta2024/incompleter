#Source: https://stackoverflow.com/questions/60049059/python-linear-regression-typeerror-invalid-type-promotion
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
data=pd.read_excel('C:\\Users\\Proximo\\PycharmProjects\Counts\\venv\\Counts.xlsx')  
data['DATE'] = pd.to_datetime(data['DATE'])
data.plot(x = 'DATE', y = 'COUNT', style = 'o')
plt.title('Corona Spread Over the Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.show()

X=data['DATE'].values.reshape(-1,1)
y=data['COUNT'].values.reshape(-1,1)
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=.2,random_state=0)
regressor = LinearRegression()  
regressor.fit(X_train,Y_train)
y_pre = regressor.predict(X_test)