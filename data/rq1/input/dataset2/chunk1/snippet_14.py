#Source: https://stackoverflow.com/questions/57702020/why-does-list-comprehension-closure-throw-nameerror-in-python-3-but-not-in-pyt
class A(object):
    a = [1, 2, 3]
    b = [n for n in a if n in a]

print(A.b)