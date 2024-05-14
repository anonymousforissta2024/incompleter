#Source: https://stackoverflow.com/questions/54719893/why-unbound-local-error-is-showing-up-where-i-expect-nameerror-should-be-raised
def func():
    x=10
    del x
    print(x)
func() #this will cause UnboundLocal Error

#But if i copy the same code and execute it without using the function call then NameError shows up

x=10
del x
print(x) #this will raise NameError as x does not exist