# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Approach 2. Using dummy node and two slow and fast ptrs
        1. Initialise dummy node with next to head because of edge case if length of ll = nth node from end
        2. Initialise slow and fast to dummy and iterate fast ptr till n (while n>0 -> n-=1)
        3. then iterate slow and fast till fast is not null (while fast.next)
        4. cut off the link slow.next = slow.next.next and return dummy.next
        Time Complexity - O(N) 
        Space Complexity - O(1)
        """
        # dummy = ListNode(0)
        # dummy.next = head
        # slow = dummy
        # fast = dummy
        # while n > 0:
        #     fast = fast.next
        #     n -= 1
        # while fast.next:
        #     slow = slow.next
        #     fast = fast.next
        # slow.next = slow.next.next
        # return dummy.next

        """
        Approach 1. Traverse to count nodes and go till 1 to count-n node to delete it
        Time Complexity - O(2N) (2 Pass)
        Space Complexity - O(1)
        """
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        if count == 1 and n == 1:  #Edge case if node is equal to length of the ll
            return None
        nEnd = 1
        itr = head
        pos = count-n
        if pos == 0:
            head = head.next
            return head
        while pos != 1:
            itr = itr.next
            pos -=1
        itr.next = itr.next.next
        return head
        
        if pos == 0:
            head = head.next
        else:
            while nEnd < pos:
                itr = itr.next
                nEnd += 1
            itr.next = itr.next.next
        return head
                
       