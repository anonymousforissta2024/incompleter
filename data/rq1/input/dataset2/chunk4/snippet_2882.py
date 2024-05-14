#Source: https://stackoverflow.com/questions/66496379/typeerror-cant-instantiate-abstract-class-ordergenaratorfortransfomer-with-abs
import numpy as np

class OrderGenaratorForTransfomer(Sequence):
    n_products = 1000
    n_windows = 10
    n_customers = 10
    def __init__(
        self
    ):
        pass

    def __getitem__(self, item):
        X = np.zeros((self.n_customers, self.n_windows, self.n_products))
        Y = np.zeros((self.n_customers, 1, self.n_products))

        return X, Y