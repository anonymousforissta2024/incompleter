#Source: https://stackoverflow.com/questions/46732047/typeerror-for-predict-probanp-arraytest
model = LogisticRegression()
model = model.fit(X, y)
test_data = [1,2,3,4,5,6,7,8,9,10,11,12,13]
test_prediction = model.predict_proba(np.array(test_data))
max = -1.0
res = 0
for i in range(test_prediction):
    if test_prediction[i]>max:
        max = test_prediction[i]
        res = i
if res==0:
    print('A')
elif res==1:
    print('B')
else:
    print('C')