#Source: https://stackoverflow.com/questions/59699242/why-does-this-produce-the-error-message-attributeerror-a-object-has-no-attrib
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def method(self):
        return A(self.x + 1, self.y + 1)

    def method2(self, f):
        if self.f().x > 3:
            return True

a = A(1, 2)
y = a.method2(a.method())
print(y)