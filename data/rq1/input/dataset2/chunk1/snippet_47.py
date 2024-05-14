#Source: https://stackoverflow.com/questions/37557411/why-does-defining-the-argument-types-for-eq-throw-a-mypy-type-error
class MyObject(object):
    def __init__(self, value: int=5) -> None:
        self.value = value

    def __eq__(self, other: MyObject) -> bool:
        return self.value == other.value