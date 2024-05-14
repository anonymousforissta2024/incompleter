#Source: https://stackoverflow.com/questions/21923652/typeerror-directoryclass-object-is-not-subscriptable-tried-de-subscripting-i
class directoryClass(): # Here we create the directory class in which we can create an object
                        # to define a directory in which we may encase files.
   Child = {}
   Parent = ''
   Referance = ''

my_picObject = directoryClass()
my_docObject = directoryClass()
userObject = directoryClass()
usersObject = directoryObject()

def my_picObj():
   my_picObject = directoryClass()
   my_picObject.Child = {'"Hello World.py"' : {'DataType' : 'Read', 'Information' : 'World'}}
   my_picObject.Parent = userObject
   my_picObject.Referance = 'My Pictures'

def my_docObj():
    my_docObject = directoryClass()
    my_docObject.Child = {'Input.py' : {'DataType' : 'Read', 'Information' : 'Hello World'}}
    my_docObject.Parent = userObject
    my_docObject.Reference = 'My Documents'

def userObj():
    userObject = directoryClass()
    userObject.Child = {'"My Documents"' : my_docObject, '"My Pictures"' : my_picObject}
    userObject.Parent = usersObject
    userObject.Referance = 'User'

def usersObj():
    usersObject = directoryClass()
    usersObject.Child = {'User' : userObject}
    usersObject.Parent = 'None'
    usersObject.Referance = 'Users'

my_picObj()
my_docObj()
userObj()
usersObj()

print = usersObject.Child['User']['"My Pictures"']['"Hello World.py"']['Information'] #Error Occurs here

print(print)