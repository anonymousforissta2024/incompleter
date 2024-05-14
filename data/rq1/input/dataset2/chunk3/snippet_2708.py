#Source: https://stackoverflow.com/questions/41342720/python-3-5-type-hinting-gives-attributeerror-module-iterator-function-has-no
from abc import ABC, abstractclassmethod
import iterator_function

class FunctionDispatcher(ABC):
    @abstractclassmethod
    def dispatch(self, function : iterator_function.IteratorFunction):
        pass