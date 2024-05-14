#Source: https://stackoverflow.com/questions/23679092/typeerror-int-argument-must-be-a-string-or-a-number-not-list-please
testfile = open(fname, 'r+')
new_ingrediants = input("How Many People Do You Want To Recalculate For?")
new_ingrediants = int(new_ingrediants)
ingrediant1 = open(fname).readlines(3)
ingrediant1 = int(ingrediant1)
new_ingrediant1 = (ingrediant1*new_ingrediants)
print (new_ingrediant1)