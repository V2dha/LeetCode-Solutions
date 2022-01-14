# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertLL(self, head):
        arr = []
        itr =  head
        while itr:
            arr.append(itr.val)
            itr = itr.next
        return arr
    
    def buildTree(self, arr):
        if not arr:
            return 
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.buildTree(arr[:mid])
        root.right = self.buildTree(arr[mid+1:])
        return root
        

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        1. Get the Middle of the linked list and make it root
        2. Recursively do same for the left half and right
            a. get the middle of the left half and make it left child of the root created in step 1
            b. get the middle of the right half and make it the right child of the root created in step 1
        """
        if not head:
            return 
        arr = self.convertLL(head)
        return self.buildTree(arr)
        
        
        
        