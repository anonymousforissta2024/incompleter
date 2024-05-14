#Source: https://stackoverflow.com/questions/57485751/nameerror-name-anyname-is-not-defined
from Resources.LinkedList import *

class Node:
    def __init__(self,name):
        self.name = name
        self.children = LinkedList()
        self.next = None