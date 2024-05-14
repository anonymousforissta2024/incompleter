#Source: https://stackoverflow.com/questions/60774729/im-getting-a-ufunctypeerror-when-doing-a-linear-regression-with-sklearn
print(X.dtype)
print(y.dtype)

lin_reg = LinearRegression()
lin_reg.fit(X, y)
print("Score: " + str(lin_reg.score(X,y)))
print("Coefs: " + str(lin_reg.coef_))
print("Intercept: " + str(lin_reg.intercept_))