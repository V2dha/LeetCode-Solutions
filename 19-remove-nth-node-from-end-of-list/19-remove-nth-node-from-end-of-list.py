# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
            
        if count == 1 and n == 1:
            return None
        
        
        nEnd = 1
        itr = head
        pos = count - n
        
        if pos == 0:
            head = head.next
            
        else:
            while nEnd < pos:
                itr = itr.next
                nEnd += 1
            itr.next = itr.next.next
        return head
                
       