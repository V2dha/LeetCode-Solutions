# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        """
        self.maxSum = float("-inf")
        def recurseUtil(root):
            if not root:
                return 0

            left = recurseUtil(root.left)
            right = recurseUtil(root.right)
            self.maxSum = max(self.maxSum, left+right+root.val)
            return max(left+root.val, right+root.val, 0)
        recurseUtil(root)
        return self.maxSum
        