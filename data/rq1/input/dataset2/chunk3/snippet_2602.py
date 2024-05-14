#Source: https://stackoverflow.com/questions/68410926/is-there-a-way-to-solve-enter-attributeerror-in-contextdecorator
class CmTag(ContextDecorator):

    def __init__(self, cm_tag_func):
        self.cm_tag_func = cm_tag_func
        
    def __enter__(self):        
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        else:
            name = self.cm_tag_func.__name__
            print(name)

    def __call__(self, **kwargs):

        name = self.cm_tag_func.__name__
        print(name)
        print(kwargs)
        self.cm_tag_func(**kwargs)

@CmTag
def testing(**kwargs):
    pass

with testing(foo='bar') as t:
    print('a test')