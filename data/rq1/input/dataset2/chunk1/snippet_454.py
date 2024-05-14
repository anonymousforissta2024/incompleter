#Source: https://stackoverflow.com/questions/49416273/attributeerror-nonetype-object-has-no-attribute-when-creating-class
def Foo():
    a = 0
    def bar(self):
        return self.a

f = Foo()
f.bar() # error