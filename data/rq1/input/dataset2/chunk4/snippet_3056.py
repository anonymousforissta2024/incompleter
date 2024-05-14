#Source: https://stackoverflow.com/questions/64998634/getting-an-error-typeerror-str-object-cannot-be-interpreted-as-an-integer
class Name:

    def __init__(self,first,last):

      self.first = first
      self.last = last


    def __len__(self):
      return self.first

name_1 = Name('FIrst','last')

print(len(name_1))