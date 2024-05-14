#Source: https://stackoverflow.com/questions/70495575/attempting-to-alter-values-in-numpy-array-typeerror-float-object-does-not-s
self.data = self.data[self.data < self.threshold] = np.nan