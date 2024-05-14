#Source: https://stackoverflow.com/questions/59466204/probit-statsmodels-attributeerror-module-statsmodels-has-no-attribute-dis
import statsmodels

results = statsmodels.discrete.discrete_model.Probit(y, x)
print(results.summary())