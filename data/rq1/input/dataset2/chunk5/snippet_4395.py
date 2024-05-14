#Source: https://stackoverflow.com/questions/77339705/attributeerror-linkedlist-object-has-no-attribute-insert-head
class LinkedList:
    def _init_(self):
        # Empty LinkedList
        self.head = None
        # no of nodes in the LinkedList
        self.n = 0

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

    def _len_(self):
        return self.n
    
    def insert_head(self,value):
        #new node
        new_Node = Node(value)

        #Create onnection
        new_Node.next = self.head

        #Reasign head
        self.head = new_Node

        #Increment n
        self.n = self.n + 1

L = LinkedList()

L.insert_head(1)

len(L)