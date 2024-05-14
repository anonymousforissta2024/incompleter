#Source: https://stackoverflow.com/questions/62148821/overwriting-init-in-python-typeerror-init-takes-1-positional-argument
class A:
    x = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        A.x += 1

    def __init__(self):
        A.x += 1

    def displayCount(self):
        print('Count : %d' % A.x)

    def display(self):
        print('a :', self.a, ' b :', self.b)

a1 = A('George', 25000)
a2 = A('John', 30000)
a3 = A()
a1.display()
a2.display()
print(A.x)