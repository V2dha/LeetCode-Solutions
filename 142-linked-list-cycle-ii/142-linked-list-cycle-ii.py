# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach - Floyd's Cycle Finding Algorithm
        In the first iteration they will meet at k: by solving the equation we get m+k is a multiple of n.
        This suggests that it will be a full cycle at m+k.
        If the fast pointer starts again from k, it will need m to complete a full cycle or a multiple of a full cycle             Since the fast pointer has already covered k it needs m steps to complete a cycle.
        We dont know what m is. hence we start the slow pointer from the start.
        When these two pointers meet fast pointer has travelled m+k in the loop and slow has travelled m. 
        Hence we return slow as it is the start of the loop.
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow