#Source: https://stackoverflow.com/questions/56333872/adding-custom-number-class-to-python-int-results-in-typeerror
class IntType:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

# Works
print(IntType(10) + 10)

# Doesn't Work
print(10 + IntType(10))