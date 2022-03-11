# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach - 1. First find the length of ll and k = k % len
        2. Set last node's next as head
        3. Store head in temp and iterate till count-k-1
        4. Set temp.next as result and temp.next as None and return result
        Time Complexity - O(N)
        Space Complexity - 1
        """
        if not head:
            return None
        if k == 0:
            return head
        count = 1
        itr = head
        while itr.next:
            itr = itr.next
            count += 1
        k = k % count
        itr.next = head
        temp = head
        for _ in range(count-k-1):
            temp = temp.next
        result = temp.next
        temp.next = None
        return result