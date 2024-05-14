#Source: https://stackoverflow.com/questions/70101457/attributeerror-linkedlist-object-has-no-attribute-head
class LinkedList():
    def __int__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
          self.head = newNode
        else:
            #head =>john->Ben->Matthew->None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        #head=>john->Ben->Matthew->None
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
        currentNode = currentNode.next
    

# node => data, next
#firstnode.data => data, firstnode.next => None
firstNode = Node('john')
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node('Ben')
linkedlist.insert(secondNode)
thridNode = Node('Matthew')
linkedlist.insert
linkedlist.printList()