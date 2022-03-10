# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        A = ''
        B = ''
        while l1:
            A += str(l1.val)
            l1 = l1.next
        while l2:
            B += str(l2.val)
            l2 = l2.next
        A = int(A[::-1])
        B = int(B[::-1])
        C = str(A+B)
        C = C[::-1]
        
        head = ListNode(C[0])
        itr = head
        for i in range(1, len(C)):
            itr.next = ListNode(C[i])
            itr = itr.next
        return head