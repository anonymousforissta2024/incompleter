#Source: https://stackoverflow.com/questions/48830707/attributeerror-while-accessing-instance-variables
class Test():

    __class_secret_number = 100

    def __secret_func(self):
        self.number1 = 1
        self.__secret_number1 = 11
        print('You cannot see this unless accessing from the Class itself')

    def test_func(self):
        self.number2 = 2
        self.__secret_number2 = 22

    def my_func(self):
        self.__secret_func()
        print('Secret no. from class: ', self.__class_secret_number)

        print('non secret no. from secret func: ', self.number1)
        print('Secret no. from secret func: ', self.__secret_number1)

        # These two prints raise an exception.
        print('non secret no. from test_func: ', self.number2)
        print('Secret no. from test_func: ', self.__secret_number2)

test = Test()
test.my_func()