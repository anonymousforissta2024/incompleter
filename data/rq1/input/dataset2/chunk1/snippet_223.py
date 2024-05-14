#Source: https://stackoverflow.com/questions/60473871/typeerror-init-got-multiple-values-for-argument-with-python-3-using-sup
class Parent:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    #more methods that to some stuff

class Child(Parent):
    a = 1 #a and b are class attributes
    b = 2

    def __init__(self, var1 = 1, var2 = 2, var3 = None):
        super().__init__(self, var1 = 1, var2 = 2) #error shows up for this line
        self.var3 = var3

child_obj = Child(var3 = 3)