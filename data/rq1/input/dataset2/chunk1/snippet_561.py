#Source: https://stackoverflow.com/questions/26064701/appendleft-iterating-deque-function-attributeerror-list-object-has-no-attrib
from collections import deque

list_stack = []
list_queue = ([])
string_to_list = "This is a sentence with more than six words."

string_to_list = string_to_list.split()

for i in string_to_list:
    list_stack.append(i)
    list_queue.appendleft(i)
print( "The variable created as a stack" ,list_stack)
print( "The variable created as a queue" ,list_queue)