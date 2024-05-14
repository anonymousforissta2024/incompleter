#Source: https://stackoverflow.com/questions/72736760/making-abstract-property-in-python-3-results-in-attributeerror
import abc
class MyClass(abc.ABC):
    @abc.abstractmethod
    @property
    def foo(self):
        pass