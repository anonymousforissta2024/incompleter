#Source: https://stackoverflow.com/questions/61764787/attributeerror-test-object-has-no-attribute-a
class Test():
    def __int__(self):
        self.a = 1

t = Test()
print(t.a)