# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach 2 - In place sorting by using l1 and manipulating next pointers
        Time Complexity - O(N+M)
        Space Complexity - O(1)
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val: #in case l1 > l2
            list1, list2 = list2, list1  
            
        l1, l2 = list1, list2
        res = l1  #to send the head of merged ll
        while l1 and l2:
            temp = None
            while l1 and l1.val <= l2.val:
                temp = l1
                l1 = l1.next
            temp.next = l2
            l1, l2 = l2, l1 
        return res
        
        """
        Approach 1 - Create another ll using 2 sorted ll
        1. Time Complexity - O(N+M)
        2. Space Complexity - O(N+M)
        """
        dummy = ListNode(0)
        p = dummy
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return dummy.next
                