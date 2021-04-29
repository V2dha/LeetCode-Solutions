# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = 0
        itr = head
        while itr:
            l += 1
            itr = itr.next
        index = l-n
        if index == 0:
            head = head.next
        count = 0
        itr = head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        return head