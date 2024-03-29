# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if head is None:
        #     return 
        # itr = head
        # while itr.next:
        #     if itr.val == itr.next.val:
        #         itr.next = itr.next.next
        #         if itr.next == None:
        #             break
        #     else:    
        #         itr = itr.next
        # return head
        if head is None:
            return head
        curr = head
        while curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head