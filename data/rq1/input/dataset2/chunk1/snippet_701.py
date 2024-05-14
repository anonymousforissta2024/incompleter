#Source: https://stackoverflow.com/questions/56850716/typeerror-when-extending-a-class-with-additional-attributes
class inheritest(bytes):
    def __init__(self, bs: bytes, x: int = 0):
        print("child class init")
        self.x = x
        super().__init__(bs)


print(inheritest(b'foobar', 3))