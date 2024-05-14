#Source: https://stackoverflow.com/questions/67916291/pd-dataframe-resulting-in-typeerror-when-a-metaclass-is-defined-before-it
class Test(Mapping): 
    x = 1
    y = 2
    z = 3

'x' in Test           # True
list(Test.items())    # [('x', 1), ('y', 2), ('z', 3)]
{**Test}              # {'x': 1, 'y': 2, 'z': 3}