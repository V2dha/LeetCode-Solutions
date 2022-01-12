# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #Similar to iterative preorder traversal
        #in which stack can be used to append the root, root.right, and root.left keeping
        #track of the prev node
        
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
 
            
        