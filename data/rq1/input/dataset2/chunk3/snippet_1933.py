#Source: https://stackoverflow.com/questions/49614191/cx-freeze-python-3-6-typeerror-in-sklearn-file
class PicklingPool(Pool):

    def __init__(self, processes=None, forward_reducers=None,
                 backward_reducers=None, **kwargs):
        if forward_reducers is None:
            forward_reducers = dict()
        if backward_reducers is None:
            backward_reducers = dict()
        self._forward_reducers = forward_reducers
        self._backward_reducers = backward_reducers
        poolargs = dict(processes=processes)
        poolargs.update(kwargs)
        super(PicklingPool, self).__init__(**poolargs)