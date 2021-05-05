# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1 == None and l2 == None:
            return None
        while l1:
            l.append(l1.val)
            l1 = l1.next
        while l2:
            l.append(l2.val)
            l2 = l2.next
        l.sort(reverse=True)
        s = ListNode(l[0], None)
        for i in range(1, len(l)):
            node = ListNode(l[i], s)
            s = node
        return s