#Source: https://stackoverflow.com/questions/67413780/error-while-rewriting-repr-typeerror-expected-0-arguments-got-1
class node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    def add(self, nod):
        self.children.append(nod)
leaf_1 = [1,4,3]
leaf_2 = [2,5,3]
leaf_3 = [4,4,3]
leaf_4 = [5,5,5]
tree = parent = node(leaf_1)
parent.add(leaf_2)
parent.add(leaf_3)
parent.add(leaf_4) 
print(tree) # no error without this line