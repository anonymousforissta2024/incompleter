#Source: https://stackoverflow.com/questions/46502885/why-does-using-super-in-a-call-method-on-a-metaclass-raise-typeerror
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        new_cls = type.__new__(cls, name, bases, attrs)
        return new_cls

    def __call__(cls, *args, **kw):
        ### why the 'super()' here raises TypeError: 'ListMetaclass' object is not iterable
        return super().__call__(cls, *args, **kw)
        return super(__class__, cls).__call__(cls, *args, **kw)
        return super(__class__, cls.__class__).__call__(cls, *args, **kw)

class MyList(list, metaclass=ListMetaclass):
    a=1
    def bar(self):
        print('test');

L=MyList()
L.add(1)
print('Print MyList :', L)