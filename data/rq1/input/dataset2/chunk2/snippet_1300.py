#Source: https://stackoverflow.com/questions/48447149/typeerror-in-tensorflow-scipyoptimizerinterface-when-using-in-keras
class CGTFOptimizer(object):
    def compute_gradients(self, loss, params):
        optimizer = ScipyOptimizerInterface(loss, method='cg')
        result = optimizer.minimize(loss)
        return result

class CGTF(TFOptimizer):
    """ Wrapper for TFOptimizer """
    def __init__(self):
       super(CGTF, self).__init__(optimizer=CGTFOptimizer())