# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        itr = head
        l = []
        while itr:
            if itr in l:
                return True
            else:
                l.append(itr)
            itr = itr.next
        return False