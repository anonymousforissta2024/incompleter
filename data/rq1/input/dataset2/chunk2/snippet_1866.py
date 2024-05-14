#Source: https://stackoverflow.com/questions/67554168/python-decorator-on-class-typeerror-super-argument-1-must-be-type-not-funct
import functools
registry = {}

def register(name=None):
    """A decorator for registering modules
    :param name: (optional) name for component
    """
    def _wrap_func(func):
        registry[name or func.__name__] = func

        @functools.wraps(func)
        def _wrap_args(*args, **kwargs):
            return func(*args, **kwargs)

        return _wrap_args
    return _wrap_func

class Base:

    def __init__(self, arg):
        self.arg = arg

@register(name="module1")
class Module1(Base):

    def __init__(self, arg):
        super(Module1, self).__init__(arg=arg)
        # super().__init__(arg=arg)

@register(name="module2")
class Module2(Base):

    def __init__(self, arg):
        super(Module2, self).__init__(arg=arg)