# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        
        while curr.next and curr.next.next:
            first = curr.next
            sec = curr.next.next
            curr.next = sec
            first.next = sec.next
            sec.next = first
            curr = curr.next.next
            
            
        return dummy.next
        