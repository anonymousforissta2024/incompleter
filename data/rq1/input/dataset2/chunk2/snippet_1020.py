#Source: https://stackoverflow.com/questions/70590761/get-attribute-error-while-calling-a-attribute-of-specific-class-in-another-class
class Class1:
    def __init__(self,a ,b) -> None:
        self.a = a
        self.b = b


class Class2:
    def __init__(self, myobject) -> None:
        self.myobject = myobject

    def __eq__(self, other: object) -> bool:
        return self.myobject.a == other.a

    def __str__(self) -> str:
        return str(self.myobject)

variable1=Class2(Class1(1,2))
variable2=Class2(Class1(1,3))

print(variable1==variable2)