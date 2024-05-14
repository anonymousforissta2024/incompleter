#Source: https://stackoverflow.com/questions/69636611/attributeerror-super-object-has-no-attribute-word-weighting
class FLSA(FTM):
    def __init__(self, word_weighting='normal'):
        super().__init__(word_weighting = word_weighting)
        self.sparse_global_term_weighting = super().get_sparse_global_term_weights(word_weighting = super().word_weighting)
        