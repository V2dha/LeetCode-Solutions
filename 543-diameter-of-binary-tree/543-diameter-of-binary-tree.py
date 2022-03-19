# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Approach - Get left depth and right depth and add them
        return maximum of the diameter, left depth + right depth
        Time Complexity - O(N)
        Space Complexity - O(1) + O(H) Recursion Stack
        """
        self.diameter = 0
        def getDiameter(root):
            if not root:
                return 0
            left = getDiameter(root.left)
            right = getDiameter(root.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right)+1
     
        getDiameter(root)
        return self.diameter
        