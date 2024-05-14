from functools import reduce
from operator import getitem

def test(d, selectors):
    return reduce(getitem, selectors, d)
print(test(users, ['Carla ', 'name', 'last']))
print(test(users, ['Carla ', 'postIds', 1]))