#Source: https://stackoverflow.com/questions/60774729/im-getting-a-ufunctypeerror-when-doing-a-linear-regression-with-sklearn
x_sample = X[:144]
y_sample = y[:144]

print("Predictions: " + lin_reg.predict(x_sample))