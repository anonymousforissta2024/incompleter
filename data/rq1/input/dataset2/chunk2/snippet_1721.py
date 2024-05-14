#Source: https://stackoverflow.com/questions/59481545/add-two-numbers-problem-linked-list-python-leetcode-attributeerror
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    a = l1 #pointers
    b = l2 #pointers
    arr1 = []
    arr2 = []

    while a.next is not None:
      arr1.append(a.val)
      a = a.next
    arr1.append(a.val) #storing the values of linked lists in arrays/lists

    while b.next is not None:
      arr2.append(b.val)
      b = b.next
    arr2.append(b.val) #storing the values of linked lists in arrays/lists

    rev1 = reversed(arr1) #reversed list
    rev2 = reversed(arr2) #reversed list

    inta = "".join(str(rev1)) #converting list to strings
    intb = "".join(str(rev2))

    c = str(inta + intb) #performing addition - the answer we wanted
    revc = reversed(c) #answer in string form - reversed (output in string at present)

    #trying to convert into linked list and return it
    q = l1
    for i in revc:
      q.val = i
      q = q.next
    return l1