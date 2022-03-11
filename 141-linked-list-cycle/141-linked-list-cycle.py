# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Two Pointer Approach - slow goes by 1 pointer and fast goes by 2 pointer if the there is no cycle then both the pointers can never be equal. Eg - 1-2-3-4-5-6-3
        Time Complexity = O(N)
        Space Complexity = O(1)
        """
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        # """
        # Time Complexity = O(N) since the time to search in dictionary is O(1)
        # Space Complexity = O(N) due to dictionary
        # """
        # if not head:
        #     return False
        # itr = head
        # hmap = {}
        # while itr:
        #     if itr in hmap:
        #         return True
        #     else:
        #         hmap[itr] = 1
        #     itr = itr.next
        # return False