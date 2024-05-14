#Source: https://stackoverflow.com/questions/62506069/typeerror-missing-1-required-positional-argument
import scipy.optimize as optimize 
optimal_sharpe=optimize.minimize(minimize_sharpe,
                                 initializer,
                                 method = 'SLSQP',
                                 bounds = bounds,
                                 constraints = constraints)
print(optimal_sharpe)