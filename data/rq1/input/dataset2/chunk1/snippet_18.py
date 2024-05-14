#Source: https://stackoverflow.com/questions/48136025/typeerror-multiple-bases-have-instance-lay-out-conflict
from collections import defaultdict, OrderedDict
class owndic(OrderedDict, defaultdict):
    pass