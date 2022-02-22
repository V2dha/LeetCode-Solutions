# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Using Divide and Conquer Merge Sort
        Time Complexity = O(nlogk)
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(left, right)
    
    def merge(self, l, r):
        temp = ListNode()
        p = temp
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return temp.next
        