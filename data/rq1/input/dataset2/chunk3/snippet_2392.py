#Source: https://stackoverflow.com/questions/55840738/attributeerror-module-main-has-no-attribute-averagewordlengthextractor
class AverageWordLengthExtractor(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        pass
    def average_word_length(self, text):
        return np.mean([len(word) for word in text.split( ) if word not in stopWords])
    def fit(self, x, y=None):
        return self
    def transform(self, x , y=None):
        return pd.DataFrame(pd.Series(x).apply(self.average_word_length)).fillna(0)