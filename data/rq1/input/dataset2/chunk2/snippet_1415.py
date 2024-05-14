#Source: https://stackoverflow.com/questions/46503572/typeerror-required-argument-not-found-getitem-numpy
import numpy as np

class Myarray (np.ndarray):
    def __getitem__(self,n):
       if n<0:
          raise IndexError("...")
       return np.ndarray.__getitem__(self,n)

class Items(Myarray):
    def __init__(self):
       self.load_tab()

class Item_I(Items):
    def load_tab(self):
       self.tab=np.load("file.txt")

a=Item_I()