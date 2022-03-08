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
        hmap = {}
        while itr:
            if itr in hmap:
                return True
            else:
                hmap[itr] = 1
            itr = itr.next
        return False