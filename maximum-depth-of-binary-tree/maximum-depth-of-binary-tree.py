# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ldepth = self.maxDepth(root.left)
        rdepth = self.maxDepth(root.right)
        return max(ldepth, rdepth)+1
        