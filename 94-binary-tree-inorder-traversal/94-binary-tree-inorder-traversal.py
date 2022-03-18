# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ele = []
        self.solve(root, ele)
        return ele
    
    def solve(self, root, ele):
        if not root:
            return 
        if root.left:
            self.solve(root.left, ele)
        ele.append(root.val)
        if root.right:
            self.solve(root.right, ele)
        