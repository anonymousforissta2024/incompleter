#Source: https://stackoverflow.com/questions/60919797/python3-nameerror-variable-not-defined
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        i = 0
        def inOrder(root):
            global i
            if root == None:
                return
            inOrder(root.left)
            i += 1
            if i == k:
                return
            inOrder(root.right)

        inOrder(root)
        return i