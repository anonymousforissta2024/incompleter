#Source: https://stackoverflow.com/questions/61314183/attributeerror-node-object-has-no-attribute-data
class Node:
    def _init_ (self, left, right, data):
        self.left = None
        self.right = None
        self.data = list () #Using a list for people with the same first name
def addGuest (root, guest) : #Defining left requirements
    if guest < root.data [0] :
        if root.left == None:
            root.left = Node ()
            root.left.data.append (guest)
        else:
            addGuest (root.left, guest)
    else: #Defining right requirements
        if guest > root.data [0] :
            if root.right == None:
                root.right = Nide ()
                root.right.data.append (guest)
            else:
                addGuest (root.right, guest)
        else:
            root.right.data.append (guest)
def printGuest(root) :
    if root == None:
        return
    print(root.data)
    printGuest (root.left) #printing left and right so both sides of the room are represented.
    printGuest (root.right)
root = Node()
root.data.append("M") #M is halfway through the alphabet. Depending on the group, this may need to change
for i in range (0,8): #Choosing 8 to ensure it divides evenly. This can be changed
        addGuest (root, input("Add Guest"))
print ("Left side:")
printGuest (root.left)
print("Right Side:")
printGuest (root.right)