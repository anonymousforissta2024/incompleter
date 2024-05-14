#Source: https://stackoverflow.com/questions/73985803/i-was-trying-to-add-elements-in-a-linked-list-in-python-but-i-am-getting-typeer
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count+1
            itr = itr.next
        print(count)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1

if __name__ == '__main__':
    root = linked_list() 
    root.insert_at_begining(5)
    root.insert_at_begining(15)
    root.insert_at_begining(10)
    root.insert_at_end(34)
    root.insert_at(2, 31)
    root.insert_at_end(45)
    root.print()
    root.get_length()