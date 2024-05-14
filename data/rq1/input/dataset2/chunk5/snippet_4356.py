#Source: https://stackoverflow.com/questions/67336013/name-error-self-not-defined-when-calling-a-function-to-create-in-class-vari
class Documents:
    def __init__(self, input_file):
        self.input_file_ = input_file #List in which each element is a list of tokens
        
        assert type(self.input_file_) is list, 'Input file is not a list'
        assert type(self.input_file_[0]) is list, 'Elements in input file are not lists' #Only checks first instance, not all. But should suffice
                
    def get_vocabulary(self):
        vocabulary = set([el for lis in self.input_file_ for el in lis])
        return vocabulary, len(vocabulary) 
    
    vocabulary, vocabulary_size = self.get_vocabulary()