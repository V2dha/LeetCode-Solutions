# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Approach - 1. First find the length of ll and k = k % len
        2. Set last node's next as head
        3. Store head in temp and iterate till count-k-1
        4. Set temp.next as result and temp.next as None and return result
        Time Complexity - O(N)
        Space Complexity - O(1)
        """
        if not head:
            return None
        if k == 0:
            return head
        count = 1
        itr = head
        while itr.next:
            itr = itr.next
            count += 1
            
        k = k % count
        
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        itr.next = head
        
        temp = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        for _ in range(count-k-1):
            temp = temp.next
            
        result = temp.next
        temp.next = None
        return result