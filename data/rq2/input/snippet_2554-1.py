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

    def get_node(self, index):
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                return None
        return current

def has_cycle(llist):
    slow = llist.head
    fast = llist.head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
a_llist = LinkedList()
for data in data_list:
    a_llist.append(int(data))
length = len(data_list)
if length != 0:
    values = '0-' + str(length - 1)
    last_ptr = input('Enter the index [' + values + '] of the node to which you want the last node to point (enter nothing to make it point to None): ').strip()
    if last_ptr == '':
        last_ptr = None
    else:
        last_ptr = a_llist.get_node(int(last_ptr))
        a_llist.last_node.next = last_ptr
if has_cycle(a_llist):
    print('The linked list has a cycle.')
else:
    print('The linked list does not have a cycle.')