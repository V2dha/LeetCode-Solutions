# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        else:
            itr = head
            l = []
            while itr:
                l.append(itr.val)
                itr = itr.next
            if l[::-1] == l:
                return True
            else:
                return False
        