class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list:

    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def delete_item(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next

    def iterate_item(self):
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
print('Original list:')
for val in items.iterate_item():
    print(val)
print('\nAfter removing the first item from the list:')
items.delete_item('PHP')
for val in items.iterate_item():
    print(val)