#Source: https://stackoverflow.com/questions/57096886/why-typeerror-str-object-is-not-callable-error-has-occurred-in-my-code
def uppercase(func_one):
    func_one = func_one()
    return func_one.upper()

def split(func_two):
    func_two = func_two()
    return func_two.split()

@split

@uppercase    
def CallFunction():
    return "my string was in lower case"

res = CallFunction()
print(res)