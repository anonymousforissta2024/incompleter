#Source: https://stackoverflow.com/questions/52546940/attributeerror-type-object-has-no-attribute
class starts:

    def __init__(self, ans, a, b):

        self.ans = input("Please type the operation to do the function as below \n 1. Sum \n 2. Subtract \n 3. multiply \n 4. divide \n")
        self.a = int(input("please enter the number you want to do the operation with : "))
        self.b = int(input("please enter the number you want to do the operation with : "))


class maths(starts):
    def __init__(self, sum, subtract, divide, multiply):

        self.sum = sum
        self.subtract = subtract
        self.divide = divide
        self.multiply = multiply

        def sum(self, a, b):
            print (self.a + self.b)
    #
        def subtract(self, a, b):
            print(self.a - self.b)
    #
        def divide(self, a, b):
            print(self.a / self.b)
    #
        def multiply(self, a, b):
            print(self.a * self.b)


class operations(maths):

    def __init__(self, class_a):

        #super(operations,self).__init__(self.ans, self.a, self.b)
        super().__init__(self.ans, self.a, self.b)

        self.ans = class_a.ans

        if class_a.ans == self.sum:
            print(starts.maths.sum(self.a, self.b))

        elif class_a.ans == self.subtract:
            print(starts.maths.subtract(self.a, self.b))

        elif class_a.ans == self.divide:
            print(starts.maths.divide(self.a, self.b))

        else:
            class_a.ans == self.multiply
            print(starts.maths.multiply(self.a, self.b))


starts.maths.operations()