#Source: https://stackoverflow.com/questions/56009288/typeerror-object-of-type-int-has-no-len-in-python-on-atom-editor
def celsius_to_farhenheit(C):
    if(type(C)=='int'):
        return ("Not possible to find out its length")
    else:
        return (len(C))


print(celsius_to_farhenheit(10))