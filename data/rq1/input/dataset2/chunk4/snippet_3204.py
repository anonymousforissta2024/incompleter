#Source: https://stackoverflow.com/questions/74298573/getting-an-error-in-binary-tree-question-attributeerror-int-object-has-no-at
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        li = []
        curr = root
        li.append([root.val])
        if curr.right and curr.left:
            li.append([self.levelOrder(curr.left.val), self.levelOrder(curr.right.val)])
        elif not curr.right and curr.left:
            li.append([self.levelOrder(curr.left.val)])
        elif curr.right and not curr.left:
            li.append([self.levelOrder(curr.right.val)])
#            elif not curr.right and not curr.left:
        else:
            return li