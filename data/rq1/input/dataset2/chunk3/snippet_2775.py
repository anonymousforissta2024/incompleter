#Source: https://stackoverflow.com/questions/41342720/python-3-5-type-hinting-gives-attributeerror-module-iterator-function-has-no
import function
import function_dispatcher

class IteratorFunction(function.Function):
    def accept(self, dispatcher : function_dispatcher.FunctionDispatcher):
        dispatcher.dispatch(self)