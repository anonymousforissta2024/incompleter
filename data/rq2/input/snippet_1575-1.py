from types import FunctionType
f_func = FunctionType(f_code.co_consts[0], globals(), 'gfg')
print(f_func())