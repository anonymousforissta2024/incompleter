#Source: https://stackoverflow.com/questions/45901265/receiving-attributeerror-exit-even-when-with-object-has-exit-defined
class Builder:
    def __init__(self):
        print("Builder init fires")

    def __getattr__(self, name):
        return Element(name, self)

class Element:
    def __init__(self, name, builder):
        self.name = name
        self.builder = builder
        print("Element init fires for name of", self.name)
    def __call__(*args, **kargs):
        print("CALL fires, now with attributes listed:")
        for attr, value in sorted(kargs.items()):
            print(' %s=>%s' % (attr, value))

    def __enter__(self):  
        return self

    def __exit__(self, type, value, traceback): 
        pass

aa = Builder()        
with aa.feed(xmlns='http://www.w3.org/2005/Atom'):
    print("INSIDE THE WITH")