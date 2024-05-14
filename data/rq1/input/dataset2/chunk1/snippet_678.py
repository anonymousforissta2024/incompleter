#Source: https://stackoverflow.com/questions/34500737/typeerror-object-takes-no-parameters-with-python2-metaclass-converted-to-py
#!/usr/bin/env python3
# test3.py

class Meta(type):
    def __new__(mcs, name, bases, clsdict):
        new_class = type.__new__(mcs, name, bases, clsdict)
        return new_class

class Root(object, metaclass=Meta):
    def __init__(self, value=None):
        self.value = value
        super(Root, self).__init__()

class Sub(Root):
    def __init__(self, value=None):
        super(Sub, self).__init__(value=value)

    def __new__(cls, value=None):
        super(Sub, cls).__new__(cls, value)

if __name__ == '__main__':
    sub = Sub(1)