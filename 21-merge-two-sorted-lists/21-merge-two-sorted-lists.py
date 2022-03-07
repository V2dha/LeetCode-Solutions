# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None
        l = []
        itr1 = list1
        itr2 = list2
        
        while itr1:
            l.append(itr1.val)
            itr1 = itr1.next
        
        while itr2:
            l.append(itr2.val)
            itr2 = itr2.next
            
        l.sort(reverse=True)
        head = ListNode(l[0])
        for i in range(1, len(l)):
            node = ListNode(l[i],head)
            head = node
        return head
            