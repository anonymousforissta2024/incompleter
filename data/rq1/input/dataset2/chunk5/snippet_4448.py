#Source: https://stackoverflow.com/questions/60990112/typeerror-fit-takes-1-positional-argument-but-3-were-given
class MyClass (BaseEstimator, ClassifierMixin):

    def __init__(self, FilePath1, FilePath2):
        self.fp1 = FilePath1
        self.fp2 = FilePath2

    #Return self nothing else to do here    
    def fit( self, X = None, y = None ):
        return self 

    def transform( self, X, y = None ):
        return X