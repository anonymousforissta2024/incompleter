#Source: https://stackoverflow.com/questions/66584134/how-to-remove-typeerror-module-object-is-not-callable-in-glm
import statsmodels.api as sm 
glm=sm(y_train, X_train, family=sm.families.Gaussian())