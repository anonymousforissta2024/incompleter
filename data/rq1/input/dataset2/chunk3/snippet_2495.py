#Source: https://stackoverflow.com/questions/56551423/attributeerror-int-object-has-no-attribute-data
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.leftChild is None:
                    self.leftChild = Node(data)
                else:
                    self.leftChild.insert(data)
            elif data > self.data:
                if self.rightChild is None:
                    self.rightChild = Node(data)
                else:
                    self.rightChild.insert(data)
        else:
            self.data = data

    def traverseLevelOrder(self):
        queue = []
        queue.append(self.data)
        while queue:
            # Print front of queue and remove it from queue
            print(queue[0].data)
            temp = queue.pop(0)

            # Enqueue left child
            if temp.leftChild is not None:
                queue.append(temp.leftChild)

            # Enqueue right child
            if temp.rightChild is not None:
                queue.append(temp.rightChild)


class BST:
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if self.rootNode is None:
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def traverseLevelOrder(self):
        if self.rootNode is None:
            return
        else:
            self.rootNode.traverseLevelOrder()


bst = BST()
bst.insert(2)
bst.insert(4)
bst.insert(1)
bst.insert(3)
bst.traverseLevelOrder()