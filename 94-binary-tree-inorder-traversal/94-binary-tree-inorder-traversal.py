# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach 1. Using Recursion
        1. Initialise empty list to store vals and then call solve function passing list and root
        2. Declare solve function with paramenters root and ele
        3. if not root -> return 
        4. 
        """
        ele = []
        self.solve(root, ele)
        return ele
    
    def solve(self, root, ele):
        if not root:
            return 
        self.solve(root.left, ele)
        ele.append(root.val)
        self.solve(root.right, ele)
        