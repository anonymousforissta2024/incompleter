#Source: https://stackoverflow.com/questions/62174465/typeerror-dict-object-is-not-callable-with-ordereddict-and-multiple-inheritan
from collections import OrderedDict
from abc import ABC, abstractmethod

class Dumpable(ABC):
    def __init__(self):
        self.dump_settings = None
        super().__init__()

    def dump_settings(self, settings ):
        self.dump_settings = settings
        pass


class ItemSet(OrderedDict, Dumpable):
    def __init__(self , allow_substitution : bool = False ):
        super(OrderedDict, self).__init__()
        super(Dumpable,  self).__init__()
        # also substituting two calls above with the
        # following, do not change behavior:
        # super().__init__()
        self.allow_substitution = allow_substitution
        pass

    def dump_settings(self,settings):
        super().dump_settings(settings)
        pass

itemset = ItemSet()
output = open("output.txt", "w", encoding="utf-8")
d= dict( output = output , html = False )
print(repr(d))
# this call seems to have no problems:
itemset.dump_settings(d)
print(repr(d))
# note that the given error "'dict' object is not callable"
# has nothing to do with 'd' param because if you change
# in the followin the 'd' with a non-dictionary object,
# the error remains, for example:
# itemset.dump_settings('hello')
itemset.dump_settings(d)
output.close()