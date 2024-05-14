#Source: https://stackoverflow.com/questions/72751187/attributeerror-function-object-has-no-attribute-issubtree-for-recursive-fun
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def is_the_same(s, t):

            if not s and not t:
                # both s and t are empty
                return True

            elif s and t:
                # both s and t are non-empty
                # keep checking in DFS
                return s.val == t.val and is_the_same(s.left, t.left) and is_the_same(s.right, t.right)

            else:
                # one is empty, the other is non-empty
                return False

        # -----------------------------------------------------------
        return bool(s and t) and (is_the_same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

t3 = TreeNode(3)
t3.left = TreeNode(4)
t3.right = TreeNode(5)
t3.left.left = TreeNode(1)
t3.left.right = TreeNode(2)

t4 = TreeNode(4)
t4.left = TreeNode(1)
t4.right = TreeNode(2)

a = Solution.isSubtree(self, t3,t4)
print(a)