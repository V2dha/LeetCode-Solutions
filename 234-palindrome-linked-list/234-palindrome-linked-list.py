# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Approach -
        1. First find middle of ll using slow and fast ptr
        2. Then reverse the ll from slow (create separate func for reverse)
        3. Then take start = head and iterate till slow is not null
        4. if start.val != slow.val then return false else keep moving slow and start
        5. return True in the end
        Time Complexity - O(N/2)+O(N/2)+O(N/2)
        Space Complexity - O(1)
        """
        slow = head
        fast = head
        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse ll from slow
        slow = self.reverse(slow)
        
        #start from head and val 
        start = head
        while slow:
            if start.val != slow.val:
                return False
            start = start.next
            slow = slow.next
        return True
            
            
        