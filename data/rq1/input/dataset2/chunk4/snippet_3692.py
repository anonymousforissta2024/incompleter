#Source: https://stackoverflow.com/questions/71117282/why-am-i-getting-an-type-error-in-my-python-generator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # self.next is the next node to be returned when "next" is called, or None
    # when exhausted
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self.traverse( root )
        self.next = next( self.iter )

    def next(self) -> int:
        assert self.hasNext()
        node = self.next
        try:
            self.next = next( self.iter )
        except StopIteration:
            self.next = None
        return node        

    def hasNext(self) -> bool:
        return self.next != None 
    
    def traverse( self, node ):
        if node != None:
            yield from self.traverse( node.left )
            yield node.val
            yield from self.traverse( node.right )

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()