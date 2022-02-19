# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Approach - Recursion DFS
        Time Complexity and Space Complexity = O(N)
        """
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, path):
        if not root:
            return 0
        if not root.left and not root.right:
            path = path*10 + root.val
            self.res += path
        self.dfs(root.left, path*10+root.val)
        self.dfs(root.right, path*10+root.val)
        
        # """
        # Approach : DFS with Stack
        # Time Complexity = O(N) 
        # Space Complexity = O(N)
        # """
        # if not root:
        #     return 0
        # stack = []
        # stack.append(root)
        # res = 0
        # while stack:
        #     node = stack.pop()
        #     if not node.left and not node.right:
        #         res += node.val
        #     if node.right:
        #         node.right.val += node.val*10
        #         stack.append(node.right)
        #     if node.left:
        #         node.left.val += node.val*10
        #         stack.append(node.left)
        # return res
