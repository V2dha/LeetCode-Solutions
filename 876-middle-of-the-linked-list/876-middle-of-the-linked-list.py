# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        
        midItr = head
        midCount = 0
        while midItr:
            if midCount == count//2:
                return midItr
            midItr = midItr.next
            midCount += 1
        return midItr