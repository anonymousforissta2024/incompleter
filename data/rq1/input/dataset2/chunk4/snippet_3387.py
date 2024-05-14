#Source: https://stackoverflow.com/questions/73979950/attribute-error-in-linkedlist-implementation
class Node():

 def __init__(self, value):
  self.value = value
  self.next = None

class LinkedList():

 def __init__(self):
  self.head = None
  self.tail = None

 def append(self, value):
  new_node = Node(value)
  if self.head == None:
   self.head = new_node
   self.tail = self.head
   self.length = 1
  else:
   self.tail.next = new_node
   self.tail = new_node 
   self.length += 1

 def prepend(self,value):
  new_node = Node(value)
  if self.head == None:
   self.head = new_node
   self.tail = self.head
   self.length += 1
  else:
   new_node.next = self.head 
   self.head = new_node
   self.length += 1

 def insert(self, index, value): 
  new_node = Node(value)
  if index>=self.length:
   self.append(value)
   return
  elif index < 1:
   self.prepend(value)
   return
  else:
   header = self.traverseToIndex(index-1)
   pointer= self.traverseToIndex(index-1).next 
   header.next = new_node 
   new_node.next = pointer 
   self.length += 1

 def traverseToIndex(self, index):
  counter = 0
  current_node = self.head
  while counter<=index:
   current_node = self.next 
   counter += 1
  return current_node 
 
 def printl(self):
  temp = self.head
  while temp != None:
   print(temp.value , end = ' ')
   temp = temp.next
   print()
  print('Length = '+str(self.length)) 

l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(3,99)