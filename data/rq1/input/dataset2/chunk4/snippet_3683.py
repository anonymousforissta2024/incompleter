#Source: https://stackoverflow.com/questions/62344903/getting-nameerror-name-self-is-not-defined-while-executing-the-following-pr
class inputoutstring(object):

    def __init__(self):
        self.s = ""

class getstring(self):
    self.s = input("Enter the string for printing")

class printstring(self):
    print(self.s.upper())

str_obj = inputoutstring()

str_obj.getstring()

str_obj.printstring() 