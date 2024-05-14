#Source: https://stackoverflow.com/questions/44555302/why-is-there-a-nameerror-in-this-list-comprehension
class A(object):
    integers = [1, 2, 3]
    singles = [i for i in integers]

class B(object):
    integers = [1, 2, 3]
    pairs = [(i, j) for i in integers for j in integers]