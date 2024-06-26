class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

def print_middle(llist):
    current = llist.head
    length = 0
    while current:
        current = current.next
        length = length + 1
    current = llist.head
    for i in range((length - 1) // 2):
        current = current.next
    if current:
        if length % 2 == 0:
            print('The two middle elements are {} and {}.'.format(current.data, current.next.data))
        else:
            print('The middle element is {}.'.format(current.data))
    else:
        print('The list is empty.')
a_llist = LinkedList()
for data in data_list:
    a_llist.append(int(data))
print_middle(a_llist)