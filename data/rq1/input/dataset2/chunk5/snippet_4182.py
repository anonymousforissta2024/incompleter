#Source: https://stackoverflow.com/questions/64168242/error-nameerror-name-self-is-not-defined-even-though-i-declare-self
class AdaBoost_regressor():
    def __init__(self, n_estimators, functions):
        # n_estimators is the number of weak regressors     
        self.n_estimators = n_estimators
        
        # We will store the sequence of functions in object "functions"
        self.functions = np.array([None] * n_estimators, dtype = 'f')
    
    # We set f_0 = 0
    def f_0(x):
        return 0
    self.functions[0] = f_0