#Source: https://stackoverflow.com/questions/31895302/python3s-super-and-comprehensions-typeerror
class A(object):
    def __repr__(self):
         return "hi!"  

class B(A):
    def __repr__(self):
         return "".join(super().__repr__() for i in range(2))  

repr(B())
#output: <repr(<__main__.B at 0x7f70cf36fcc0>) failed: TypeError: super(type, obj): obj must be an instance or subtype of type>

class C(A):
    def __repr__(self):
        s = ''
        for i in range(4):
            s += super().__repr__()
        return s     

repr(C())
#output: hi!hi!hi!hi!

class D(A):
    def __repr__(self):
        return "".join(super(D,self).__repr__() for i in range(4))

repr(D())
#output: hi!hi!hi!hi!