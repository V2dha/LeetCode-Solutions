# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 1. Using Recursion
        """
        preorder = []
        self.solve(root, preorder)
        return preorder
    
    def solve(self, root, preorder):
        if not root:
            return 
        preorder.append(root.val)
        self.solve(root.left, preorder)
        self.solve(root.right, preorder)