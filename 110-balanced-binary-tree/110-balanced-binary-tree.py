# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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