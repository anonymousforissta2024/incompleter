#Source: https://stackoverflow.com/questions/58208539/get-methods-name-using-getattribute-without-type-error
class Person(object):
    def __init__(self):
        super()

    def test(self):
        print(1)

    def __getattribute__(self, attr):
        print(attr)



p = Person()

p.test()