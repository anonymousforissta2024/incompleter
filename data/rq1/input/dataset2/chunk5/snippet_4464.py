#Source: https://stackoverflow.com/questions/59626524/typeerror-a-class-meth-missing-1-required-positional-argument-a-class-meth
class A():
    def __init__(self,init_var):
        self.init_var = init_var

    def A_class_meth(self, A_class_meth_var1):
        print("run")

class B():
    def Start(self):        
        self.B_class_var = A("NAME")
        A.A_class_meth(self.B_class_var)

var = B()
var.Start()