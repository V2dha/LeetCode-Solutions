# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 2 - Use slow and fast pointer (Similar to detect loop in LL)
        1. Initialise slow and fast to head
        2. while fast and fast.next -> move slow by 1 and fast by 2
        3. By the time fast reaches end slow would be at middle
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
        
       
        """
        Approach 1 - Iterate through ll once and count total nodes
        2. Iterate again and break when midCount == count//2 
        3. Return the midItr
        Time Complexity - O(N) + O(N/2) (Two Traversals)
        Space Complexity - 1
        """
        if not head:
            return head
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        
        mid = count//2
        itr = head
        while mid:
            itr = itr.next
            mid -= 1
        return itr
        
        midItr = head
        midCount = 0
        while midItr:
            if midCount == count//2:
                return midItr
            midItr = midItr.next
            midCount += 1
        return midItr