# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Approach - Similar to height of tree just return 1 as soon as tree is unbalanced
    if check(node) == -1 then it is unbalanced else balanced
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            
            if abs(left-right) > 1 or left == -1 or right == -1:
                return -1
            
            return max(left,right)+1
        return True if check(root) != -1 else False
        
        
    """
    Approach 1. By finding height for every left and right subtree and then checking
    Time Complexity - O(N*N) n for traversing and n for height
    """
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right)+1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh) > 1:
            return False
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if not left or not right:
            return False 
        return True