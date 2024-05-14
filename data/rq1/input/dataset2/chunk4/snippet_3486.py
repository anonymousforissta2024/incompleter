#Source: https://stackoverflow.com/questions/76178464/typeerror-when-using-lru-cache-with-class-inheritance-in-python-3-8
from functools import lru_cache

@lru_cache(1)
class A:
    def __init__(self):
        pass

@lru_cache(1)
class B(A):
    pass

b = B()