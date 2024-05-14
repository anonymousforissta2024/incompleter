#Source: https://stackoverflow.com/questions/70562802/inheritance-from-parent-class-return-attribute-error
class MathParent:
    def multiply(self, number1, number2):
        self.answer = number1 * number2
        return self.answer
    def happy(self):
        return "Nice Mark!"

class MathChild(MathParent):
    def plus_x(self, x) :
        return self.answer + x

p_out = MathParent()
print(p_out.multiply(5, 2))
print(p_out.happy())

c_out = MathChild()
print(c_out.happy())
print(c_out.plus_x(5))