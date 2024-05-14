#Source: https://stackoverflow.com/questions/51239898/can-we-use-closure-in-python-for-nested-function-but-it-is-giving-me-nameerror
def outerFunction(func): 
    def add(x,y):
        print(x+y)

    def sub(x,y):
        print(x-y)

    return func

calc_add=outerFunction(add)
calc_sub=outerFunction(sub)
calc_add(56,60)
calc_sub(56,7)