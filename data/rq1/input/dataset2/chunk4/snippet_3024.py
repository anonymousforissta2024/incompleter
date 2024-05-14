#Source: https://stackoverflow.com/questions/76069846/register-function-raising-a-nameerror-when-referencing-the-class
class Quantity:

    _CONVERT_FUNCS = []

    def __register_conversion(func):
        Quantity._CONVERT_FUNCS.append(func)
        return func

    @__register_conversion
    def function1(a, b):
        return a + b

    @__register_conversion
    def function2(a, b):
        return a * b