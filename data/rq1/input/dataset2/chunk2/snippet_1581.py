#Source: https://stackoverflow.com/questions/56090708/why-am-i-getting-attributeerror-linearregressiongd-object-has-no-attribute-n
class LinearRegressionGD (object):

    def _init_(self, eta=0.001, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w = np.zeros(1 + X.shape[1])
        self.cost_ = {}

        for i in range(self.n_iter):
            output = self.net_input (X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return self.net_input(X)

    X = racing[["BSP"]].values
    y = racing[["Position"]].values
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X_std = sc_X.fit_transform(X)
    y_std = sc_y.fit_transform(y)
    lr = LinearRegressionGD()
    lr.fit(X_std, y_std)