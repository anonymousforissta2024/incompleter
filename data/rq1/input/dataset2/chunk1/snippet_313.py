#Source: https://stackoverflow.com/questions/68554023/typeerror-init-subclass-takes-no-keyword-arguments-related-to-subclass-an
from abc import ABC, abstractmethod

class Pipeline(ABC):  

    @abstractmethod
    def read_data(self):
        pass
    
    def __init__(self, **kwargs):        
        self.raw_data = self.read_data()        
        self.process_data = self.raw_data[self.used_cols]

   
class case1(Pipeline):
    def read_data(self):
        return pd.read_csv("file location") # just hard coding for the file location
       
    @property
    def used_cols(self):
        return ['col_1', 'col_2','col_3','col_4']