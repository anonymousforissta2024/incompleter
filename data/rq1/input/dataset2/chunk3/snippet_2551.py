#Source: https://stackoverflow.com/questions/57486229/why-is-there-an-attribute-error-inside-the-condition-of-the-while-loop-but-no
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        while l1.val != None and l2.val != None:
            if l1.val >= l2.val:
                result.append(l2.val)
                l2 = l2.next
            else:
                result.append(l1.val)
                l1 = l1.next
        if l1.val != None:
            while l1.val != None:
                result.append(l1.val)
                l1 = l1.next
        else:
            while l2.val != None:
                result.append(l2.val)
                l2 = l2.next
        return result