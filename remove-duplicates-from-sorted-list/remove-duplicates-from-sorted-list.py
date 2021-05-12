# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return 
        itr = head
        while itr.next:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
                if itr.next == None:
                    break
            else:    
                itr = itr.next
        return head