#Source: https://stackoverflow.com/questions/61834959/patsyerror-error-evaluating-factor-nameerror-name-wheel-is-not-defined
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd


cars = pd.concat([y_train, X_train], axis = 1)
cars.head()
model = smf.ols(formula ='price ~ symboling + wheel-base + length + width + height + curb-weight + engine-size + bore + stroke + compression-ratio + horsepower + peak-rpm + city-mpg + highway-mpg + cylinder',data=cars)
results = model.fit()
print(results.summary())