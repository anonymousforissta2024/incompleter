#Source: https://stackoverflow.com/questions/76214437/attributeerror-modeldata-object-has-no-attribute-design-info
import statsmodels.api as sm
import numpy as np

# define the data
x1 = np.random.rand(100)
x2 = np.random.rand(100)
y = 2*x1 + 3*x2 + np.random.normal(size=100)

# build the model with all independent variables
X = sm.add_constant(np.column_stack((x1, x2)))
model = sm.OLS(y, X).fit()

# perform the F-test
f_value, p_value, _ = sm.stats.anova_lm(model, typ=1)