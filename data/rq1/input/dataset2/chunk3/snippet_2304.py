#Source: https://stackoverflow.com/questions/67415057/python-add-a-method-with-parameters-with-class-decorator-results-in-typeerror
class MyInp(int):
    pass

def add_bar(cls, input_type):
    def bar(self, inp :input_type):
        print(f"bar: {inp}")

    setattr(cls, 'bar', bar)
    return cls

@add_bar(input_type=MyInp)
class Foo():
   pass

f = Foo()
f.bar(3)