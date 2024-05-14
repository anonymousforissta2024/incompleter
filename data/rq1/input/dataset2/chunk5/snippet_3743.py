#Source: https://stackoverflow.com/questions/60320610/nameerror-name-is-not-defined
class Solution:
    def rob(root: TreeNode) -> int:
        sum = [0, 0]
        add(root, sum, 0)
        if sum[0] < sum[1]:
            return sum[1]
        else:
            return sum[0]

    def add(node: TreeNode, sum: List[int], index: int):
        if not node:
            return
        sum[index] += node.val
        index += 1
        if index >= len(sum):
            index = 0;
        add(node.left, sum, index)
        add(node.right, sum, index)