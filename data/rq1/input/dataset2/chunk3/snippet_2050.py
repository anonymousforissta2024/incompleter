#Source: https://stackoverflow.com/questions/62721117/continuous-typeerror-function-object-is-not-subscriptable-in-python-3-8
x = 0
df, mavg, start = getStock(companyName='AAPL', month=24, plot=True)

dayslist = []
while x != 7:
    day = start + dateutil.relativedelta.relativedelta(days=x)
    dayslist.append(int(day.strftime('%Y%m%d')))
    x += 1

dates = np.array(dayslist)
prediction_out = 7

df['Prediction'] = df.shift(-prediction_out)
print(df.tail())

x = np.array(df.drop(['Prediction']))
y = np.array(df["Prediction"])
x = x[:-prediction_out]
y = y[:-prediction_out]

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

svm_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svm_rbf.fit(x_train, y_train)

svm_confidence = svm_rbf.score(x_test, y_test)
print('SVM confidence is {}.'.format(svm_confidence))

x_forecast = np.array(df.drop(['Prediction']))[-prediction_out:]
print(x_forecast)

fPlotList = []
x = 0
while x != 7:
    fPlotList.append(x_forecast[x])
    x += 1

plt.plot[fPlotList, dayslist]
plt.show()