#Source: https://stackoverflow.com/questions/67916291/pd-dataframe-resulting-in-typeerror-when-a-metaclass-is-defined-before-it
import pandas as pd
class MappingMeta(type, collections.abc.Mapping):
    ... # same as above

class Mapping(metaclass=MappingMeta):
    pass


class Test(Mapping):
    x = 1
    y = 2

print(pd.DataFrame({'x': [1, 2]}))