from functools import reduce
from operator import getitem

def get(d, selectors):
    return reduce(getitem, selectors, d)
print(get(users, ['freddy', 'name', 'last']))
print(get(users, ['freddy', 'postIds', 1]))