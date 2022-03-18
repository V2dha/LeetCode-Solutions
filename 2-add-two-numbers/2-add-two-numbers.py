# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach -
        1.
        Time Complexity - O(max(N, M))
        Space Complexity - O(N)
        """
        start = ListNode(0)
        temp = start
        carry = 0
        while l1 or l2 or carry:
            csum = 0
            if l1:
                csum += l1.val
                l1 = l1.next
            if l2:
                csum += l2.val
                l2 = l2.next
            csum += carry
            carry = csum//10
            node = ListNode(csum%10)
            temp.next = node
            temp = temp.next
            
        return start.next
            
        """
        Approach 1 : Using lists
        """
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