# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        itr = head
        count = 1
        while itr.next:
            itr = itr.next
            count += 1
            
        k = k%count
        
        itr.next = head
        
        temp = head
        for _ in range(count-k-1):
            temp = temp.next
            
        result = temp.next
        temp.next = None
        return result
        