# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        l = []
        if head is None:
            return None
        else:
            itr = head
            while itr:
                l.append(itr.val)
                itr = itr.next
        l = l[::-1]
        C = ListNode(l[0])
        curr=C
        for i in range(1,len(l)):
            curr.next=ListNode(l[i])
            curr=curr.next
        return C
            
            
        