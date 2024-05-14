#Source: https://stackoverflow.com/questions/61058868/why-am-i-getting-a-nameerror-for-self-name
class foo:

    def __init__(self, name):
        self.name = name
    print(self.name)

x = foo('it works')