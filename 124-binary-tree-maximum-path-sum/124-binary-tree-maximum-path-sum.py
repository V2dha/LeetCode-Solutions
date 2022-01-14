# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Approach - 
        1. Maintain a global maxSum which will store the maximum cumulative sum so far
        2. Recurse through left and right subTrees and update the maxSum i.e. left+right+root.val only if it is greater than maxSum
        3. Return the maximum out of left children + root.val, right children + root.val or 0 in order to prevent adding negative numbers
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
        