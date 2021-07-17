# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.elements = []
        self.solve(root)
        return self.elements
    
    def solve(self, root):
        if root is None:
            return 
        self.solve(root.left)
        self.elements.append(root.val)
        self.solve(root.right)
        
            