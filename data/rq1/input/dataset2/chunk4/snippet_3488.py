#Source: https://stackoverflow.com/questions/46284357/python-subclass-attribute-error
class socialNetwork:
    class node:
        def __init__(self, name, friendList):
            self.name=name
            self.friendList=friendList

        def __init__(self):
            self.nodeList=[]

        def addPerson(self, name, friendList):
            person=self.node(name,friendList)
            self.nodeList.append(person)

s = socialNetwork()
s.addPerson("John",["Alice","Bob"])
s.addPerson("Alice",["John","Bob","Jeff"])
s.addPerson("Bob",["John","Alice","Jeff","Ken"])
s.addPerson("Jeff",["Alice","Bob","Barbra"])
s.addPerson("Ken",["Bob","Barbra"])
s.addPerson("Barbra",["Jeff","Ken"])
for person in s.nodeList:
    print("name: ",person.name, "\n\t friends: ",person.friendList)