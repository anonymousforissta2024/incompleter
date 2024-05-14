#Source: https://stackoverflow.com/questions/28692702/attributeerror-type-object-x-has-no-attribute-y-and-some-other-inconsistencies
# data hiding
class Fruit:
    __price = 0

    def show(self):
        self.__price += 1
        print (self.__price)

objFruit = Fruit()
objFruit.show()
objFruit.show()
objFruit.show()
print (objFruit._Fruit.__price) # error