#Source: https://stackoverflow.com/questions/14583761/typeerror-module-init-takes-at-most-2-arguments-3-given
import Object

class Visitor(Object):
    pass

instance = Visitor()  # this line throws the exception