# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        def right(root, level, max_level, ans):
            if not root:
                return
            if max_level[0] < level:
                ans.append(root.val)
                max_level[0] = level
            right(root.right, level+1, max_level, ans)
            right(root.left, level+1, max_level, ans)
        max_level = [0]
        right(root, 1, max_level, ans)
        return ans
        