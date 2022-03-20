# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Approach 1. Using Recursion 
        Time Complexity - O(N) Space Complexity - O(N)
        """
        if not root:
            return 
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
        
        #Similar to iterative preorder traversal
        #in which stack can be used to append the root, root.right, and root.left keeping
        #track of the prev node
        """
        Approach 2. Using stack
        Time Complexity - O(N) Space Complexity - O(N)
        """
        if not root:
            return  
        rootStack = []
        prev = None
        rootStack.append(root)
        while rootStack:
            node = rootStack.pop()
            #append right child first so that left child is traversed first
            if node.right:
                rootStack.append(node.right)
            if node.left:
                rootStack.append(node.left)
            if prev is not None:
                prev.right = node
                prev.left = None
            prev = node
 
            
        